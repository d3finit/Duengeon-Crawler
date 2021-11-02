class Log():
	def __init__(self):
		import logging
		from datetime import date
	
		today = date.today()
		self.logger = logging
		self.logger.basicConfig(
			filename=f'logs/{today.strftime("%d-%m-%Y")}.log', 
			filemode='a', 
			format='%(asctime)s [%(process)d/%(levelname)s]: %(message)s', 
			datefmt='[%H:%M:%S]',level=logging.DEBUG)
		
	def info(self,msg):
		self.logger.info(msg)

	def err(self,msg):
		self.logger.error(msg)
	
	def db(self,msg):
		self.logger.debug(msg)

	def wrn(self,msg):
		self.logger.warning(msg)

	def crit(self,msg):
		self.logger.critical(msg)