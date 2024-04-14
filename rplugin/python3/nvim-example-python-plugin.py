import pynvim

@pynvim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @pynvim.function('TestFunc')
    def doItPython(self, args):
        self.vim.command('echo "hello from python"')
