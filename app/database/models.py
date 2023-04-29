# import datetime
# import pytz

# from typing import Dict, List, NamedTuple, ByteString
# from app.database import db 


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text, BLOB
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class TgUser(Base):
    __tablename__ = "usertg"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    id_chat = Column(Integer, nullable=False, unique=True)
    password = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=False)
    last_name = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)
    first_name = Column(String, nullable=False)
    photo_url = Column(Boolean, nullable=False)
    is_bot = Column(Boolean, nullable=False)
    language_code = Column(String, nullable=False)


    # items = relationship("Item", back_populates="owner")


class Product(Base):
	__tablename__ = "product"

	id = Column(Integer, primary_key=True)
	name = Column(String)
	attribute = Column(String)
	description = Column(Text)
	price = Column(Integer)       #dels.PositiveIntegerField(verbose_name='Стоимость')
	slug = Column(String)       #dels.CharField(max_length=80, verbose_name='Алиас')
	category = Column(String)       #escription = Column(String, unique=True, index=True)tring, index=True)
	src = Column(String)

	product_photo = relationship("ProductPhoto", back_populates="item_prod")

class ProductPhoto(Base):
	"""docstring for product_photo"""
	__tablename__ = "product_photo"

	id = Column(Integer, primary_key=True)
	image = Column(BLOB)
	url = Column(String)
	id_product = Column(Integer, ForeignKey("product.id"))

	item_prod = relationship("Product", back_populates="product_photo")
                                





#	inserted_row_id=db.insert("tguser", {
# 	"codename": new_user['username'],
# 	"id_chat": new_user['id'],
# 	"created": _get_now_formatted(),
# 	"last_name": new_user['last_name'],
# 	"first_name": new_user['first_name'],
# 	"photo_url": new_user['photo_url'],
# 	"is_bot": new_user['is_bot']
# 	})
# 	tg_user_data = {i[0]: i[1] for i in new_user.items() if (i[0] != 'id') and (i[0] != 'username')}

# 	return TgUser(codename=None, id_chat=None, tg_user_data =tg_user_data)


# def tg_user_is_db(user_data: dict) ->bool:
# 	codename = str(user_data['username'])
# 	cursor = db.get_cursor()
# 	try:
# 		cursor.execute(f"select * from tguser where codename='{codename}'" )
# 	except Exception as e:
# 		print(e)
# 		return False
	          
# 	result = cursor.fetchone()
# 	print (result)
# 	if result == None:
# 		return False
# 	TgUser.codename = result[0]
# 	TgUser.id_chat = result[1] 
# 	TgUser.last_name = result[3] 
# 	TgUser.first_name = result[4] 
# 	TgUser.photo_url = result[5] 
# 	TgUser.is_bot = result[6]
# 	return True

# def _get_now_formatted() -> str:
#     """Возвращает сегодняшнюю дату строкой"""
#     return _get_now_datetime().strftime("%Y-%m-%d %H:%M:%S")

# def _get_now_datetime() -> datetime.datetime:
#     """Возвращает сегодняшний datetime с учётом времненной зоны Мск."""
#     tz = pytz.timezone("Europe/Moscow")
#     now = datetime.datetime.now(tz)
#     return now

# def convert_to_binary_data(filename):
#     # Преобразование данных в двоичный формат
#     with open(filename, 'rb') as file:
#         blob_data = file.read()
#         print(type(file))
#     return blob_data



# def write_to_file(data, filename):
#     # Преобразование двоичных данных в нужный формат
#     with open(filename, 'wb') as file:
#         file.write(data)
#     print("Данные из blob сохранены в: ", filename, "\n")

# def get_img_product(emp_id):
# 	product_data = db.fetchall(
# 		"product", "id name description price slug".split()
# 	)
# 	for item in product_data:
# 		if item['id'] == emp_id:
# 			print("colon = ", type(item), "value = ")
# 			return item


# class Product(NamedTuple): # таблица Товаров
# 	name: str #= models.CharField(max_length=50, verbose_name='Название')
# 	attribute: List[str]
# 	description: str #= models.TextField(null=True, blank=True, verbose_name='Описание')
# 	price: int #= models.PositiveIntegerField(verbose_name='Стоимость')
# 	slug: str #= models.CharField(max_length=80, verbose_name='Алиас')
# 	category: str

# 	#section #= models.ForeignKey('Section', on_delete=models.CASCADE, verbose_name='Раздел') # связь один ко многим с таблицой разделов
# 	#reviews #= models.ManyToManyField('Review', related_name='Product', verbose_name='Отзывы', through='ReviewProductRelation') # связь многие ко многим с таблицой Отзывов


# def row_is_db(table: str, col: tuple) ->Product:
# 	cursor = db.get_cursor()
# 	try:
# 		cursor.execute(f"select * from {table} where {col[0]}='{col[1]}'" )
# 	except Exception as e:
# 		print("Ошибка при работе с SQLite", e)
# 		return None
	          
# 	result = cursor.fetchone()
# 	print (135, result)
# 	if result == None:
# 		return None
# 	Product.id = result[0],
# 	Product.name = result[1],
# 	Product.description = result[2],
# 	Product.price = result[3],
# 	Product.slug = result[4]
# 	Product.category = result[5],
# 	Product.attribute = result[6],
# 	return Product

# def add_product(new_product: dict):
# 	try:
# 		inserted_row_id=db.insert("product", {
# 		"name": new_product['name'],
# 		"attribute": new_product['attribute'],
# 		"description": new_product['description'],
# 		"price": new_product['price'],
# 		"category": new_product['category'],
# 		"slug": new_product['slug']
# 		})
# 	except Exception as e:
# 		print("Ошибка при работе с SQLite", e)
# 	product_data = {i[0]: i[1] for i in new_product.items()}
# 	return Product(name=new_product['name'], attribute=new_product['attribute'], description=new_product['description'], price=new_product['price'], slug=new_product['slug'] , category=new_product['category'])#codename=None, id_chat=None, tg_user_data =tg_user_data)

# 	class Meta: # как будут отображаться в админке
# 		verbose_name = 'Товар'
# 		verbose_name_plural = 'Товары'

# 	class ProductPhoto(NamedTuple):
# 		"""docstring for product_photo"""
# 		image: bytes
# 		url: str

# 		# def __init__(self, arg):
# 		# 	super(ProductPhoto, self).__init__()
# 		# 	self.arg = arg
# 	def __str__(self): # для красивого вывода
# 	  return self.name


# def add_img_product(photo: dict ) -> bool:
# 	filename_img = photo['url']
# 	blob_data_img = convert_to_binary_data(filename_img)
# 	inserted_row_img=db.insert_blob("product", ("id", 1), ("image", blob_data_img))
# 	print('lol',  inserted_row_img)
# 	return True


# class Order(NamedTuple): # таблица Заказов
# 	id_n: int   # = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Автор') # связь один ко многим с Пользователем
# 	product: List[str]   # = models.ManyToManyField('Product', related_name='Order', verbose_name='Товары', through='OrderProductRelation') # связь многие ко многим с таблицой Товаров
# 	total: int   # = models.PositiveIntegerField(verbose_name='Общая стоимость заказа')
# 	user_id: int
# 	order_user_data: List[dict]
# 	complete: bool   # = models.BooleanField(default=False, verbose_name='Завершен')

# 	class Meta: # как будут отображаться в админке
# 	  verbose_name = 'Заказ'
# 	  verbose_name_plural = 'Заказы'

# 	def add_order_db(new_order: dict):
# 		inserted_row_id=db.insert("order", {
# 		"product": new_order['username'],
# 		"id_n": new_order['id'],
# 		"created": _get_now_formatted(),
# 		"total": new_order['last_name'],
# 		"count": new_order['first_name'],
# 		"user_id": new_order['first_name'],
# 		"order_user_data": new_order['photo_url'],
# 		"complete": new_order['is_bot']
# 		})
# 		db.close_ses()
# 		tg_user_data = {i[0]: i[1] for i in new_user.items() if (i[0] != 'id') and (i[0] != 'username')}

# 		return TgUser(codename=None, id_chat=None, tg_user_data =tg_user_data)


# class OrderProductRelation(models.Model): # промежуточная таблица заказ - товар
#     order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заказ') # связь один ко многим с таблицой Заказов
#     product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар') # связь один ко многим с таблицой Товаров
#     amount = models.PositiveIntegerField(verbose_name='Количество')
#     total = models.PositiveIntegerField(verbose_name='Сумма')

#     class Meta: # как будут отображаться в админке
#         verbose_name = 'Заказ-Товар'
#         verbose_name_plural = 'Заказ-Товар'

#     def __str__(self): # для красивого вывода
#         return str(self.order) + ' ' + str(self.product.name)

