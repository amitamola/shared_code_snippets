# Code create a CSV with package, their version and their license:

import pkg_resources
import pandas as pd

def get_pkg_license(pkg):
    try:
        lines = pkg.get_metadata_lines('METADATA')
    except:
        lines = pkg.get_metadata_lines('PKG-INFO')

    for line in lines:
        if line.startswith('License:'):
            return line[9:]
    return '(Licence not found)'

def print_packages_and_licenses():
    t = []
    for pkg in sorted(pkg_resources.working_set, key=lambda x: str(x).lower()):
        a,b = str(pkg).split()
        t.append((a,b,get_pkg_license(pkg)))
    return t

if __name__ == "__main__":
    final = print_packages_and_licenses()
    
pd.DataFrame(final, columns=['Package', 'Version', 'License']).to_csv('requirements.csv', index=False)
