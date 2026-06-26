import tkinter as tk
import os
from tkinter import messagebox
import random
from PIL import Image, ImageTk

def carregar_background(caminho):
    caminho_completo = os.path.join(BASE_DIR, caminho)
    imagem = Image.open(caminho_completo)

    imagem = imagem.resize((600, 500), Image.LANCZOS)

    return ImageTk.PhotoImage(imagem)



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def equipar_skin(parte, skin):
    skins_equipadas[parte] = skin
    atualizar_pet_visual()
global pet_ids



def carregar_sprite(caminho):
    caminho_completo = os.path.join(BASE_DIR, caminho)
    imagem = Image.open(caminho_completo)
    imagem = imagem.resize((200, 200))
    return ImageTk.PhotoImage(imagem)





#return ImageTk.PhotoImage(imagem)



#    return ImageTk.PhotoImage(imagem)
# =====================
# STATUS DO PET
# =====================
pet = {
    "nome": "Kumo",
    "fome": 100,
    "energia": 100,
    "felicidade": 100,
    "higiene": 100
}




pet_ids = {}

offset_y = 0
direcao = 1
olhos_fechados = False
# =====================
# FUNÇÕES
# =====================

def limitar():
    for status in pet:
        if status != "nome":

            if pet[status] > 100:
                pet[status] = 100

            if pet[status] < 0:
                pet[status] = 0

def atualizar_tela():

    fome_label.config(text=f"Fome: {pet['fome']}")
    energia_label.config(text=f"Energia: {pet['energia']}")
    felicidade_label.config(text=f"Felicidade: {pet['felicidade']}")
    higiene_label.config(text=f"Higiene: {pet['higiene']}")

def alimentar():
    pet["fome"] += 20
    limitar()
    atualizar_tela()

def dormir():
    pet["energia"] += 30
    limitar()
    atualizar_tela()

def brincar():
    pet["felicidade"] += 25
    pet["energia"] -= 10
    pet["fome"] -= 5

    limitar()
    atualizar_tela()

def banho():
    pet["higiene"] += 30
    limitar()
    atualizar_tela()

# =====================
# TEMPO PASSANDO
# =====================

def passar_tempo():

    pet["fome"] -= random.randint(1, 3)
    pet["energia"] -= random.randint(1, 2)
    pet["felicidade"] -= random.randint(1, 2)
    pet["higiene"] -= random.randint(1, 2)

    limitar()
    atualizar_tela()

    if pet["fome"] <= 0:
        messagebox.showwarning(
            "Aviso",
            "Seu pet está com muita fome!"
        )

    janela.after(3000, passar_tempo)

# =====================
# JANELA
# =====================

janela = tk.Tk()
janela.title("Pet Game")
janela.geometry("600x500")
janela.configure(bg="#222222")

janela.update() 

main_frame = tk.Frame(janela, bg="#222222")
main_frame.pack(fill="both", expand=True)

left_frame = tk.Frame(main_frame, bg="#222222")
left_frame.pack(side="left", padx=20, pady=20)

right_frame = tk.Frame(main_frame, bg="#222222")
right_frame.pack(side="right", padx=20, pady=20)

# =====================
# TÍTULO
# =====================

titulo = tk.Label(
    right_frame,
    text=pet["nome"],
    font=("Arial", 24),
    bg="#222222",
    fg="white"
)

titulo.pack(pady=20)

# =====================
# STATUS
# =====================

fome_label = tk.Label(
    right_frame,
    text="",
    font=("Arial", 14),
    bg="#222222",
    fg="white"
)

fome_label.pack(pady=5)

energia_label = tk.Label(
    right_frame,
    text="",
    font=("Arial", 14),
    bg="#222222",
    fg="white"
)

energia_label.pack(pady=5)

felicidade_label = tk.Label(
    right_frame,
    text="",
    font=("Arial", 14),
    bg="#222222",
    fg="white"
)

felicidade_label.pack(pady=5)

higiene_label = tk.Label(
    right_frame,
    text="",
    font=("Arial", 14),
    bg="#222222",
    fg="white"
)

higiene_label.pack(pady=5)

# =====================
# BOTÕES
# =====================

botao_alimentar = tk.Button(
    right_frame,
    text="Alimentar",
    font=("Arial", 12),
    width=20,
    command=alimentar
)

botao_alimentar.pack(pady=10)

botao_dormir = tk.Button(
    right_frame,
    text="Dormir",
    font=("Arial", 12),
    width=20,
    command=dormir
)

botao_dormir.pack(pady=10)

botao_brincar = tk.Button(
    right_frame,
    text="Brincar",
    font=("Arial", 12),
    width=20,
    command=brincar
)

botao_brincar.pack(pady=10)

botao_banho = tk.Button(
    right_frame,
    text="Banho",
    font=("Arial", 12),
    width=20,
    command=banho
)

botao_banho.pack(pady=10)

background = carregar_background("sprites/bg/quarto.png")
#===========================
#iae leite, passando aqui para ver se tem algo que posso ajudar :P
#==========



#============================================================
#Visual da aranha
#============================================================

#class AranhaSprites:
#    def __init__(self, canvas):
#        self.corpo = tk.PhotoImage(
#            file=os.path.join(BASE_DIR, "sprites/corpo/corpo1.png")
#        )
#        self.cabelo = tk.PhotoImage(
#            file=os.path.join(BASE_DIR, "sprites/cabelo/cabelo1.png")
#        )
#        self.rosto = tk.PhotoImage(
#            file=os.path.join(BASE_DIR, "sprites/rosto/rosto1.png")
#        )
#        self.brasos = tk.PhotoImage(
#            file=os.path.join(BASE_DIR, "sprites/brasos/brasos1.png")
#        )
#        self.pernas = tk.PhotoImage(
 #           file=os.path.join(BASE_DIR, "sprites/pernas/pernas1.png")
#        )
#============================================================
#É aqui que coloca as imagens do nosso pet guys
#============================================================

#============================================================
#agora vou fazer o dicionario"
#============================================================

skins = {
    "corpo": {
        "skin_corpo_1":
        carregar_sprite("sprites/corpo/corpo1.png"),

        "skin_corpo_2":
        carregar_sprite("sprites/corpo/corpo2.png"),

        "skin_corpo_3":
        carregar_sprite("sprites/corpo/corpo3.png")
    },

    "cabelo": {
        "skin_cabelo_1":
        carregar_sprite("sprites/cabelo/cabelo1.png"),
        "skin_cabelo_2":
        carregar_sprite("sprites/cabelo/cabelo2.png"),
        "skin_cabelo_3":
        carregar_sprite("sprites/cabelo/cabelo3.png")
    },

   
    "brasos": {
        "skin_brasos_1":
        carregar_sprite("sprites/brasos/brasos1.png"),
        "skin_brasos_2":
        carregar_sprite("sprites/brasos/brasos2.png"),
        "skin_brasos_3":
        carregar_sprite("sprites/brasos/brasos3.png")
    },

    "pernas": {
        "skin_pernas_1":
        carregar_sprite("sprites/pernas/pernas1.png"),
        "skin_pernas_2":
        carregar_sprite("sprites/pernas/pernas2.png"),
        "skin_pernas_3":
        carregar_sprite("sprites/pernas/pernas3.png")
    },
    "torso": {
        "skin_torso_1":
        carregar_sprite("sprites/torso/torso1.png"),
        "skin_torso_2":
        carregar_sprite("sprites/torso/torso2.png"),
        "skin_torso_3":
        carregar_sprite("sprites/torso/torso3.png")
    },
    "olhos": {
        "abertos": carregar_sprite("sprites/olhos/abertos.png"),
        "fechados": carregar_sprite("sprites/olhos/fechados.png")
}



}
imagem_original = Image.open(
    os.path.join(BASE_DIR, "sprites/corpo/corpo1.png")
)



imagem_redimensionada = imagem_original.resize(
    (200, 200)
)

imagem_pet = ImageTk.PhotoImage(
    imagem_redimensionada
)
print(imagem_pet.width())
print(imagem_pet.height())






skins_equipadas = {
    "corpo": "skin_corpo_1",
    "cabelo": "skin_cabelo_1",
    "brasos": "skin_brasos_1",
    "pernas": "skin_pernas_1",
    "torso": "skin_torso_1"
}
pet_ids = {}

offset_y = 0
direcao = 1

olhos_fechados = False

canvas = tk.Canvas(
    left_frame,
    width=600,
    height=500,
    bg="#222222",
    highlightthickness=0
)

canvas.pack()

background = carregar_background("sprites/bg/quarto.png")

bg_id = canvas.create_image(0, 0, image=background, anchor="nw")


def criar_pet():
    global pet_ids

    cx = canvas.winfo_width() // 2
    cy = canvas.winfo_height() // 2

    pet_ids["pernas"] = canvas.create_image(cx, cy, image=skins["pernas"][skins_equipadas["pernas"]])
    pet_ids["corpo"] = canvas.create_image(cx, cy, image=skins["corpo"][skins_equipadas["corpo"]])
    pet_ids["torso"] = canvas.create_image(cx, cy, image=skins["torso"][skins_equipadas["torso"]])
    pet_ids["brasos"] = canvas.create_image(cx, cy, image=skins["brasos"][skins_equipadas["brasos"]])
    pet_ids["cabelo"] = canvas.create_image(cx, cy, image=skins["cabelo"][skins_equipadas["cabelo"]])
    pet_ids["olhos"] = canvas.create_image(cx, cy, image=skins["olhos"]["abertos"])
#============================================================
#agora é só usar o dicionário para mostrar as imagens na tela
#============================================================

janela_skins = tk.Toplevel(janela)
janela_skins.title("Skins")
janela_skins.geometry("400x500")

tk.Label(
    janela_skins,
    text="Cabelos"
).pack()
for i in range(1, 4):

    tk.Button(
        janela_skins,
        text=f"Cabelo {i}",
        command=lambda n=i:
        equipar_skin(
            "cabelo",
            f"skin_cabelo_{n}"
        )
    ).pack(pady=5)


tk.Label(
    janela_skins,
    text="Corpos"
).pack()

for i in range(1, 4):

    tk.Button(
        janela_skins,
        text=f"Corpo {i}",
        command=lambda n=i:
        equipar_skin(
            "corpo",
            f"skin_corpo_{n}"
        )
    ).pack()
tk.Label(
    janela_skins,
    text="Braços"
).pack()

for i in range(1, 4):

    tk.Button(
        janela_skins,
        text=f"Braços {i}",
        command=lambda n=i:
        equipar_skin(
            "brasos",
            f"skin_brasos_{n}"
        )
    ).pack()
tk.Label(
    janela_skins,
    text="Pernas"
).pack()
tk.Label(
    janela_skins,
    text="Pernas"
).pack()

for i in range(1, 4):

    tk.Button(
        janela_skins,
        text=f"Pernas {i}",
        command=lambda n=i:
        equipar_skin(
            "pernas",
            f"skin_pernas_{n}"
        )
    ).pack(pady=5)

# =====================
# TORSOS
# =====================

tk.Label(
    janela_skins,
    text="Torsos"
).pack()

for i in range(1, 4):

    tk.Button(
        janela_skins,
        text=f"Torso {i}",
        command=lambda n=i:
        equipar_skin(
            "torso",
            f"skin_torso_{n}"
        )
    ).pack(pady=5)



def animar_idle():
    global offset_y, direcao

    offset_y += direcao

    if offset_y > 5:
        direcao = -1

    if offset_y < -5:
        direcao = 1

    atualizar_pet_visual()
    janela.after(120, animar_idle)

def piscar():
    global olhos_fechados

    olhos_fechados = True
    atualizar_pet_visual()

    janela.after(150, abrir_olhos)
def abrir_olhos():
    global olhos_fechados

    olhos_fechados = False
    atualizar_pet_visual()

    tempo = random.randint(2000, 5000)
    janela.after(tempo, piscar)
 
command=lambda n=i: (
    equipar_skin("corpo", f"skin_corpo_{n}"),
    atualizar_pet_visual()
)

def atualizar_pet_visual():
    cx = canvas.winfo_width() // 2
    cy = canvas.winfo_height() // 2
    y = cy + offset_y

    canvas.coords(pet_ids["pernas"], cx, y)
    canvas.coords(pet_ids["corpo"], cx, y)
    canvas.coords(pet_ids["torso"], cx, y)
    canvas.coords(pet_ids["brasos"], cx, y)
    canvas.coords(pet_ids["cabelo"], cx, y)
    canvas.coords(pet_ids["olhos"], cx, y)

    # 🔥 ESSA PARTE É O QUE ESTAVA FALTANDO
    canvas.itemconfig(pet_ids["pernas"], image=skins["pernas"][skins_equipadas["pernas"]])
    canvas.itemconfig(pet_ids["corpo"], image=skins["corpo"][skins_equipadas["corpo"]])
    canvas.itemconfig(pet_ids["torso"], image=skins["torso"][skins_equipadas["torso"]])
    canvas.itemconfig(pet_ids["brasos"], image=skins["brasos"][skins_equipadas["brasos"]])
    canvas.itemconfig(pet_ids["cabelo"], image=skins["cabelo"][skins_equipadas["cabelo"]])

    # olhos (mantém simples)
    canvas.itemconfig(
        pet_ids["olhos"],
        image=skins["olhos"]["fechados"] if olhos_fechados else skins["olhos"]["abertos"]
    )


def passar_tempo():
    pet["fome"] -= random.randint(1, 3)
    pet["energia"] -= random.randint(1, 2)
    pet["felicidade"] -= random.randint(1, 2)
    pet["higiene"] -= random.randint(1, 2)

    limitar()
    atualizar_tela()

    janela.after(3000, passar_tempo)
background = carregar_background("sprites/bg/quarto.png")



# =====================
# INICIAR
# =====================

background = carregar_background("sprites/bg/quarto.png")
bg_id = canvas.create_image(0, 0, image=background, anchor="nw")

janela.update()

criar_pet()

atualizar_tela()
atualizar_pet_visual()

passar_tempo()
animar_idle()
piscar()

janela.mainloop()