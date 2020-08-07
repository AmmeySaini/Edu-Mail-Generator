import sys
import os
import subprocess
try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
finally:
    import requests
import urllib, time
from io import BytesIO
from zipfile import ZipFile
import tarfile
try:
    from clint.textui import progress
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'clint'])
finally:
    from clint.textui import progress

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########
######## Github Repo - https://git.io/JJisT/ ########

def os_arch():
    os_arch = '32'
    if os.name == 'nt':
        output = subprocess.check_output(['wmic', 'os', 'get', 'OSArchitecture'])
        os_arch = output.split()[1].decode('utf-8').replace('-bit', '')
    else:
        output = subprocess.check_output(['uname', '-m'])
        if type(output) != str:
            output = output.decode('utf-8')
        if 'x86_64' in output:
            os_arch = '64'
        else:
            os_arch = '32'
    return os_arch

def get_platform_architecture_firefox():
    if sys.platform.startswith('linux'):
        platform = 'linux'
        architecture = os_arch()
    elif sys.platform == 'darwin':
        platform = 'mac'
        architecture = 'os'
    elif sys.platform.startswith('win'):
        platform = 'win'
        architecture = os_arch()
    else:
        raise RuntimeError('Could not determine geckodriver download URL for this platform.')
    return platform, architecture

def get_platform_architecture_chrome():
    if sys.platform.startswith('linux') and sys.maxsize > 2 ** 32:
        platform = 'linux'
        architecture = '64'
    elif sys.platform == 'darwin':
        platform = 'mac'
        architecture = '64'
    elif sys.platform.startswith('win'):
        platform = 'win'
        architecture = '32'
    else:
        raise RuntimeError('Could not determine chromedriver download URL for this platform.')
    return platform, architecture

def get_firefox_version():
    """
    :return: the version of firefox installed on client
    """
    platform, _ = get_platform_architecture_firefox()
    if platform == 'linux':
        try:
            with subprocess.Popen(['firefox', '--version'], stdout=subprocess.PIPE) as proc:
                version = proc.stdout.read().decode('utf-8').replace('Mozilla Firefox', '').strip()
        except:
            return None
    elif platform == 'mac':
        try:
            process = subprocess.Popen(['/Applications/Firefox.app/Contents/MacOS/firefox', '--version'], stdout=subprocess.PIPE)
            version = process.communicate()[0].decode('UTF-8').replace('Mozilla Firefox', '').strip()
        except:
            return None
    elif platform == 'win':
        path1 = 'C:\\PROGRA~1\\Mozilla Firefox\\firefox.exe'
        path2 = 'C:\\PROGRA~2\\Mozilla Firefox\\firefox.exe'
        if os.path.exists(path1):
            process = subprocess.Popen([path1, '-v', '|', 'more'], stdout=subprocess.PIPE)
        elif os.path.exists(path2):
            process = subprocess.Popen([path2, '-v', '|', 'more'], stdout=subprocess.PIPE)
        else:
            return
        version = process.communicate()[0].decode('UTF-8').replace('Mozilla Firefox', '').strip()
    else:
        return
    return version


def get_chrome_version():
    """
    :return: the version of chrome installed on client
    """
    platform, _ = get_platform_architecture_chrome()
    if platform == 'linux':
        try:
            with subprocess.Popen(['google-chrome', '--version'], stdout=subprocess.PIPE) as proc:
                version = proc.stdout.read().decode('utf-8').replace('Chromium', '').strip()
                version = version.replace('Google Chrome', '').strip()
        except:
            return None
    elif platform == 'mac':
        try:
            process = subprocess.Popen(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'], stdout=subprocess.PIPE)
            version = process.communicate()[0].decode('UTF-8').replace('Google Chrome', '').strip()
        except:
            return None
    elif platform == 'win':
        try:
            process = subprocess.Popen(
                ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'],
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
            )
            version = process.communicate()[0].decode('UTF-8').strip().split()[-1]
        except:
            return None
    else:
        return
    try:
        version = version.split(' ')[0]
    except:
        pass
    return version

def get_latest_geckodriver_version():
    """
    :return: the latest version of geckodriver
    """
    url = requests.get('https://github.com/mozilla/geckodriver/releases/latest').url
    if '/tag/' not in url:
        return
    return url.split('/')[-1]

def get_dwnld_url_firefox(version):
    platform, architecture = get_platform_architecture_firefox()

    if platform == 'win':
        return 'https://github.com/mozilla/geckodriver/releases/download/' + version + '/geckodriver-' + version + '-' + platform + architecture + '.zip'
    else:
        return 'https://github.com/mozilla/geckodriver/releases/download/' + version + '/geckodriver-' + version + '-' + platform + architecture + '.tar.gz'
def get_major_version(version):
    """
    :param version: the version of chrome
    :return: the major version of chrome
    """
    return version.split('.')[0]

def get_chrome_driver_v(version):
    """
    :param version: the version of chrome
    :return: the chromedriver version needed
    """
    return requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE_' + str(version)).text

def get_chrome_driver_dwnld_url(version):
    """
    :param version: the version of webdriver
    :return: download url of webdriver
    """
    platform, architecture = get_platform_architecture_chrome()

    return 'https://chromedriver.storage.googleapis.com/' + str(version) + '/chromedriver_' + platform + str(architecture) + '.zip'

def dwnld_zip_file(url, save_path, chunk_size=128):

    print('Downloading...')

    r = requests.get(url)

    total_length = int(r.headers['Content-Length'])

    if total_length is None or total_length == 0:
        print('Download failed')
        exit()

    with ZipFile(BytesIO(r.content)) as my_zip_file:
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            pass
        print('Download Successful')
        my_zip_file.extractall(save_path)

def dwnld_tar_file(url, save_path):

    print('Downloading...')

    response = requests.get(url)

    total_length = sum(len(chunk) for chunk in response.iter_content(8196))

    if total_length is None or total_length == 0:
        print('Download Failed')
        exit()

    with tarfile.open(fileobj=BytesIO(response.content), mode='r|gz') as my_tar_file:
        for chunk in progress.bar(response.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            pass
        print('Download Successful')
        my_tar_file.extractall(save_path)

######## For Chrome ########

def setup_Chrome(version):
    mjVer = get_major_version(version)
    if mjVer != None:
        print('Installed version - ' + str(mjVer))
        chromeDv = get_chrome_driver_v(mjVer)
        print('Chrome Driver Version Needed -', chromeDv)
        dwnldLink = get_chrome_driver_dwnld_url(chromeDv)

        dwnld_zip_file(dwnldLink, './webdriver')
    else:
        print('Chrome is not downloaded')


######## For Firefox ########

def setup_Firefox(firefox_ver):
    arc_user = get_platform_architecture_firefox()
    # firefox_ver = get_firefox_version()
    if firefox_ver != None:
        print('Installed verision - ' + str(firefox_ver))
        latestDriverv = get_latest_geckodriver_version()
        print('Latest geckodriver version - ' + latestDriverv)
        dwnldLink = get_dwnld_url_firefox(latestDriverv)
        if dwnldLink.endswith('.tar.gz'):
            dwnld_tar_file(dwnldLink, './webdriver')
        else:
            pass
            dwnld_zip_file(dwnldLink, './webdriver')
    else:
        print('Firefox is not installed')