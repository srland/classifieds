#!/usr/bin/env python
"""
  $Id$
"""
modules = ('adposting', 'payment', 'accounts',)

cronjobs = []
for module in modules:
	module = module+'.cron'
	try:
		mod = __import__(module)
		components = module.split('.')
		for comp in components[1:]:
			mod = getattr(mod, comp)

		cronjobs.append(mod.run)
	except AttributeError:
		pass
	except ImportError:
		pass

for cronjob in cronjobs:
	cronjob()
	

