import sys, builtins

printold = print
def prettyprint(*obj, sep="", end='\n', file=sys.stdout, flush=False):
  printold(sep.join([str(e) for e in obj]).lower(), end=end.lower(), file=file, flush=flush)
builtins.print = prettyprint