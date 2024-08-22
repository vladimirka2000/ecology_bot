import discord, os, random, requests
from key import *
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

infos = ["recycle - что и как переработать", "sorting - как правильно сортировать мусор", "immage - картинки природы"]

images = ["https://cdnn21.img.ria.ru/images/07e4/0a/1a/1581598772_0:489:2000:1614_1920x0_80_0_0_bd5a18cf6350f60dd428549f45e0856e.jpg",
           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnvAPUppLVwxPW-sefZRiZoJu-Dj1So_h8lw&s", 
           "https://news.ecoindustry.ru/wp-content/uploads/2023/06/199388309_l_normal_none-scaled.jpg"]

@bot.command()
async def help_bot(ctx):
    await ctx.send("Выберете одну из команд:")
    for i in infos:
        await ctx.send(i)


@bot.command()
async def recycle(ctx):
    recycles = {
"Бумага": "2-6 недель",
"Яблочные огрызки": "2-8 недель",
"Апельсиновые корки": "6 месяцев - 2 года",
"Газетная бумага": "6 недель - 6 месяцев",
"Картон": "2-6 месяцев",
"Деревянные предметы": "10-15 лет",
"Консервные банки": "80-100 лет",
"Пластиковые бутылки": "100-1000 лет",
"Стекло": "неопределенно долго (тысячи лет)",
"Алюминиевые банки": "80-200 лет",
"Резиновые шины": "50-80 лет",
"Одноразовые подгузники": "450-500 лет"
}

    for item, time in recycles.items():
        await ctx.send(f"{item}: {time}")

@bot.command()
async def sorting(ctx):
    sorting_rules = [
"Разделяйте отходы на следующие категории: бумага и картон, стекло, пластик, металл, органические отходы (пищевые, растительные), опасные отходы (батарейки, лампочки, краски, химикаты)",
"Промывайте и очищайте упаковку перед сортировкой, чтобы она была чистой",
"Сплющивайте и складывайте объемные предметы, чтобы они занимали меньше места",
"Выбрасывайте каждый тип отходов в соответствующий контейнер или пакет",
"Используйте многоразовые сумки и контейнеры для покупок, чтобы сократить количество одноразовой упаковки",
"Компостируйте органические отходы, если есть такая возможность",
"Сдавайте на переработку опасные отходы, такие как батарейки, лампочки, краски",
"Старайтесь покупать продукты с минимальной упаковкой или в многоразовой таре",
"Отдавайте ненужные, но еще пригодные вещи на благотворительность или в пункты приема"
]

    for rule in sorting_rules:
        await ctx.send(rule)  

@bot.command()
async def image(ctx):     
    for i in images:
        await ctx.send(i) 

bot.run(token())