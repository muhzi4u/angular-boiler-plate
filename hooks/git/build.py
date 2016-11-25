import os, sys

"""
Checks your git commit with JSHint. Only checks staged files
"""
def jshint():
    
    errors = []
    
    # get all staged files
    f = os.popen('git diff --name-only HEAD^ HEAD')
    
    for file in f.read().splitlines():

        # makes sure we're dealing javascript files
        if file.endswith('.js') and not file.startswith('node_modules/'):    	

            g = os.popen('jshint ' + file)
        
            # add all errors from all files together
            for error in g.readlines():
                errors.append(error)
    
    # got errors?
    if errors:
        for i, error in enumerate(errors):
            print error,
		
        # Abort the commit
        sys.exit(1) 
    
    print "Code Quality Checks completed!... Triggering commit..."
    # All good
    sys.exit(0) 
    
if __name__ == '__main__':
    jshint()
