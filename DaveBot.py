import discord
from discord.ext import commands



##initialize the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

class SimpleView(discord.ui.View):

    def __init__(self):
        super().__init__()  # Appelle le constructeur de discord.ui.View
        self.foo = None  # Initialise une variable d'instance

    @discord.ui.button(label="1",
                       style=discord.ButtonStyle.success)
    async def Button_1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("1")
        self.foo = 1
        
    
    @discord.ui.button(label="2",
                       style=discord.ButtonStyle.red)
    async def Button_2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("2")
        self.foo = 2
    
    
    @discord.ui.button(label="3",
                       style=discord.ButtonStyle.red)
    async def Button_3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("3")
        self.foo = 3

    @discord.ui.button(label="4",
                       style=discord.ButtonStyle.red)
    async def Button_4(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("4")
        self.foo = 4
    
    @discord.ui.button(label="5",
                       style=discord.ButtonStyle.red)
    async def Button_5(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("5")
        self.foo = 5
    
    @discord.ui.button(label="6",
                       style=discord.ButtonStyle.red)
    async def Button_6(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("6")
        self.foo = 6
    
    @discord.ui.button(label="7",
                       style=discord.ButtonStyle.red)
    async def Button_7(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("7")
        self.foo = 7
    
    @discord.ui.button(label="8",
                       style=discord.ButtonStyle.red)
    async def Button_8(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("8")
        self.foo = 8
    
    @discord.ui.button(label="9",
                       style=discord.ButtonStyle.red)
    async def Button_9(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("9")
        self.foo = 9


    async def wait_for_input(self):
        print("Attente d'une interaction...")  # Vérifie si la fonction est bien appelée
        try:
            await self.wait(timeout=30.0)  # Attend 30 secondes
            print(f"Le joueur a cliqué sur : {self.foo}")  # S'affiche si un bouton est cliqué
        except:
            print("Temps écoulé, aucune interaction.")
        

@bot.event
async def on_ready():
    print("le bot est connecté !")
    try:
        synced = await bot.tree.sync()  # Synchronisation des commandes slash
        print(f":white_check_mark: {len(synced)} commandes slash synchronisées !")
    except Exception as e:
        print(f":x: Erreur de synchronisation des commandes : {e}")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! ")

@bot.command()
async def morpion(ctx):
    view = SimpleView()
    await ctx.send(view=view)
    bot.loop.create_task(view.wait_for_input())
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def pas(ctx, arg1, arg2):
    await ctx.send(f'You passed {arg1} and {arg2}')

@bot.command()
async def button(ctx):
    view = SimpleView()
    #button = discord.ui.Button(label="Test")
    #view.add_item(button)
    
    #await view.wait()
    await ctx.send(view=view)
    async def check_view():
        await view.wait()
        if view.foo is None:
            print("Timeout")
    
        elif view.foo == 2:
            print("ok")
    
        elif view.foo == 1:
            print("Cancel operation")

    bot.loop.create_task(check_view())  # Lancer dans une tâche asynchrone
    
bot.run("TOKEN")
