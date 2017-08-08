from IPython.core.magic import (Magics, magics_class, CodeMagics, line_magic, cell_magic, line_cell_magic)
import os

@magics_class
class OkMagics(CodeMagics):
    """Magics related to Okpy"""
    @line_magic
    def ok(self, arg_s):
        """Load ok test into the current frontend.

        Usage:
            %ok [options] ok_test

            where ok_test is the name of the ok_test, NOT the relative path of the file containing the ok_test. If no file is found, automatically creates a file with a default template.

        Options:
            -n : Include user's namespace when searching for source code.
            -t [source]: Specify what template that you want to use. source should be a relative path from the notebook.
        """
        @line_magic
        def ok(self, arg_s):
            """Load ok test into the current frontend.
   
            Usage:
               %ok [options] ok_test
   
               where ok_test is the name of the ok_test, NOT the relative path of the file containing       the ok_test. If no file is found, automatically creates a file with a default template.
   
            Options:
               -n : Include user's namespace when searching for source code.
               -t <source>: Specify what template that you want to use. source should be a relative path    from the notebook.
            """
   
            opts, args = self.parse_options(arg_s, 'yns:r:') 

            #Creating relative path to tests: 
            args = 'tests/' + args 
    
            if not args: 
                raise ValueError('Missing ok_test name') 
            
            search_ns = 'n' in opts
            template = 't' in opts #TO-DO: implement template choice
            template_path = os.getcwd() + 'template.py'

            try: 
                contents = self.shell.find_user_code(args, search_ns=search_ns)
            except ValueError: 
                contents = self.shell.find_user_code(template_path, search_ns=False)

            contents = "%%writefile {}\n".format(args) + contents 

            self.shell.set_next_input(contents, replace=True)
        
