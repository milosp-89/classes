# module_class => class for modules to install/update/import single or multiple

import subprocess as sub, importlib.util as ilb

class Modules():
    
    """
    Base Class for interaction with different methods between modules/libraries\n
    * Methods:\n
    1. To install specific module/library\n
    2. To update existing module/library\n
    3. To import specific module/library
    """
    
    def __init__(self):
        pass
    
    """
    Constructor: doesent have any attributes/parameters
    """
        
    def install_module(self, module_name):
        
        """
        This method will install specified module/library\n
        :param1 module_name: this is the parameter describing module name to be installed\n
        :return: None
        """
        
        sub.call(["pip", "install", module_name])
        
        # check to see if the module is properly installed or not:
        spec = ilb.find_spec(module_name)
        if spec: print(f'The {module_name} module is installed!')
        else: print(f'The {module_name} module is NOT installed, please check typing or the module doesent exist!')

    def update_module(self, module_name):
        
        """
        This method will update specified module/library\n
        :param1 module_name: this is the parameter describing module name to be updated\n
        :return: None
        """
        
        try:
            sub.call("pip install --upgrade " + module_name)
            print(f"Module: {module_name} updated!")
        except Exception:
            print(f"Module: {module_name} NOT updated, please check if the module is properly typed or if it needs first to be installed!")
        
    def import_module(self, module_name):
        
        """
        This method will install specified module/library\n
        :param1 module_name: this is the parameter describing module name to be installed\n
        :return: it will return ==> "import module_name" string to be used for calling methods
        """
        
        try:
            module = __import__(module_name)
            print(f"Module: {module_name} imported!")
            return module
        except Exception:
            print(f"Module: {module_name} NOT imported, please check if the module is properly typed or if it needs first to be installed!")
    
    def __str__(self):
        
        """
        Dunder method to describe a Class object
        """
        
        return("Super CLass: Modules, for interactions with modules/libraries: please specify which module user wants to use.")

# Inheritance ==> from Modules() to MultipleModules:
class MultipleModules(Modules):
    
    """
    Child Class to represent different additional methods with modules/libraries\n
    * Methods:\n
    1. To install multiple modules\n
    2. To update multiple existing modules\n
    3. To import multiple specific modules
    """
    
    def __init__(self):
        pass
    
    """
    Constructor: doesent have any attributes/parameters
    """
    
    def install_multiple_modules(self, module_names_list):
        
        """
        This method will install multiple modules from acquired list of modules\n
        :param1 module_name_list: this is the parameter describing a list of module names to be installed\n
        :return: None
        """
        
        [self.install_module(mod) for mod in module_names_list]

    def update_multiple_modules(self, module_names_list):
        
        """
        This method will update multiple modules from acquired list of modules\n
        :param1 module_name_list: this is the parameter describing a list of module names to be updated\n
        :return: None
        """
        
        [self.update_module(mod) for mod in module_names_list]
        
    def import_multiple_modules(self, module_names_list):
        
        """
        This method will import multiple modules from acquired list of modules\n
        :param1 module_name_list: this is the parameter describing a list of module names to be imported\n
        :return: a dictionary of imported modules
        :hint ==> in order to call a specific module from a list of modules, user needs to utilize indexing
        """
        
        try:
            modules = {}
            for mod in module_names_list:
                modules[mod] = __import__(mod)
            return modules
        except Exception:
            print(f"Module: {mod} NOT imported, please check if the module is properly typed or if it needs first to be installed!")
        
    def __str__(self):
        
        """
        Dunder method to describe a Class object
        """
        
        return(" Child CLass: Modules, for interactions with modules/libraries: please specify which module user wants to use.")