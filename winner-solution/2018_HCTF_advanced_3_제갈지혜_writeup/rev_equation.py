import angr
 
def main():
    p = angr.Project("./Downloads/equation", load_options={'auto_load_libs': False})
    ex = p.surveyors.Explorer(find=(0x400B65, ), avoid=(0x400B71,))
    ex.run()
 
    return ex.found[0].state.posix.dumps(0).strip('\0\n')
 
if __name__ == '__main__':
    print main()
