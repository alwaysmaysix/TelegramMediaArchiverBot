#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from dublib.Methods import ReadJSON, WriteJSON


import logging
import os

#==========================================================================================#
# >>>>> СОЗДАНИЕ ПОЛЬЗОВАТЕЛЯ И ЕГО ДАННЫХ <<<<< #
#==========================================================================================#

class UserData:

	#==========================================================================================#
	# >>>>> СОЗДАНИЕ НОВОГО ПОЛЬЗОВАТЕЛЯ <<<<< #
	#==========================================================================================#

	def __CreateUser(self):
		# Создание экземпляра пользователя.
		self.__User = {
			"Size": 0,
			"Premium": False, 
			"FilesNotSave": 0
		}

		# Создание папки файлов пользователя.
		os.makedirs("Data/Files/" + self.__UserID)

		# Создание папки архивов пользователя.
		os.makedirs("Data/Archives/" + self.__UserID)

		# Сохранение файла пользователя.
		self.save()

	#==========================================================================================#
	# >>>>> КОНСТРУКТОР <<<<< #
	#==========================================================================================#
		
	def __init__(self, UserID: str):

		#---> Генерация статических свойств.
		#==========================================================================================#
		# ID пользователя.
		self.__UserID = str(UserID)
		
		# Данные пользователя.
		self.__User = None

		#---> Инициализация пользователя.
		#==========================================================================================#
		# Список названий файлов в директории пользователя.
		Files = list()

		# Получение списка файлов в директории.
		Files = os.listdir("Data/Users")
		
		# Фильтрация только файлов формата JSON.
		Files = list(filter(lambda x: x.endswith(".json"), Files))

		# Если пользователя не существует.
		if self.__UserID + ".json" not in Files:
			self.__CreateUser()

		# Иначе читаем данные пользователя.
		else:
			self.__User = ReadJSON("Data/Users/" + self.__UserID + ".json")

	#==========================================================================================#
	# >>>>> ПОЛУЧЕНИЕ ID ПОЛЬЗОВАТЕЛЯ <<<<< #
	#==========================================================================================#
			
	def getUserID(self) -> str:
		return self.__UserID

	#==========================================================================================#
	# >>>>> СОХРАНЕНИЕ ДАННЫХ ПОЛЬЗОВАТЕЛЯ <<<<< #
	#==========================================================================================#

	def save(self):
		# Сохранение файла пользователя.
		WriteJSON("Data/Users/" + self.__UserID + ".json", self.__User)

	#==========================================================================================#
	# >>>>> ОБНОВЛЕНИЕ ДАННЫХ ПОЛЬЗОВАТЕЛЯ <<<<< #
	#==========================================================================================#

	def __UpdateSizeUser(self, UpdatingSize: int, Premium: bool, FilesNotSave: list) -> dict:
		self.__User = {
			"Size": UpdatingSize,
			"Premium": Premium, 
			"FilesNotSave": FilesNotSave
		}

		# Сохранение файла пользователя.
		self.save()

		logging.info(f"Размер скачанных файлов: {UpdatingSize} добавлен в JSON.")
		return self.__User
