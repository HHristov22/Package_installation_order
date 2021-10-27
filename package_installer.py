import json

# Load package requires from JSON file


def load_data():
    """
    Looad information for package
    """
    with open('package.JSON') as package_file:
        data = json.load(package_file)

    return data

# Which packages needs to install main package


def requires_packages(data, list_packages):

    for package_to_install in list_packages:
        for package in data["pms"]:
            if package["name"] == package_to_install:
                index_main_package = list_packages.index(package_to_install)

                """
                Checks if a package needs other packages
                """
                if package["requires"]:
                    added_pack_for_install = False
                    for req_pack in package["requires"]:

                        """
                        Check if some package need installation on early stage
                        """
                        if req_pack not in list_packages:
                            list_packages.insert(index_main_package, req_pack)
                            index_main_package += 1
                            added_pack_for_install = True
                        else:
                            index_copy = list_packages.index(req_pack)
                            if index_copy > index_main_package:
                                print(list_packages)
                                list_packages.remove(req_pack)
                                list_packages.insert(
                                    index_main_package, req_pack)
                                print(list_packages, "\n")

                    """
                    Is it added new package for installation
                    """
                    if added_pack_for_install:
                        requires_packages(data, list_packages)
                else:
                    break

    return list_packages


"""
Check package name which want to install exist
"""


def existing_package(data, package_name):
    exist = False
    for package in data["pms"]:
        if package["name"] == package_name:
            exist = True
            break
    return exist


"""
Test for order
result on line 106
"""


def order_test(installed_packages, data):
    data = load_data()
    for installed_package in reversed(installed_packages):
        for package in data["pms"]:
            if package["name"] == installed_packages:
                index_main = installed_packages.index(installed_package)
                if package["requires"]:
                    for requires_packages in package["requires"]:
                        index_req_packages = installed_packages.index(
                            requires_packages)
                        if index_main < index_req_packages:
                            return False

    return True


"""
Install package
"""


def install_package(package):
    data_dic = load_data()
    if existing_package(data_dic, package):
        list_install = [package]
        list_requires = requires_packages(data_dic, list_install)
        print(list_requires)
        # print(order_test(list_requires, data_dic), "\n")
    else:
        print(f"This package '{package}' didi't exist.")


package_name = input()

"""
The installation order is from left to right
"""
install_package(package_name)
