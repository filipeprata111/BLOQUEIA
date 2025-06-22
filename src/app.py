import os
import platform
import tkinter as tk
from tkinter import messagebox

# Caminho do arquivo hosts dependendo do sistema operacional
HOSTS_PATH = {
    "Windows": r"C:\Windows\System32\drivers\etc\hosts",
    "Linux": "/etc/hosts",
    "Darwin": "/etc/hosts"  # macOS
}[platform.system()]

REDIRECT_IP = "127.0.0.1"

# Funções principais
def bloquear_site():
    url = entrada.get().strip()
    if not url:
        messagebox.showwarning("Entrada inválida", "Digite um endereço de site.")
        return

    try:
        with open(HOSTS_PATH, 'r+') as file:
            conteudo = file.read()
            if url in conteudo:
                messagebox.showinfo("Já bloqueado", f"O site '{url}' já está bloqueado.")
            else:
                file.write(f"\n{REDIRECT_IP} {url}\n")
                messagebox.showinfo("Sucesso", f"Site bloqueado: {url}")
    except PermissionError:
        messagebox.showerror("Permissão negada", "Execute o programa como administrador/root.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def desbloquear_site():
    url = entrada.get().strip()
    if not url:
        messagebox.showwarning("Entrada inválida", "Digite um endereço de site.")
        return

    try:
        with open(HOSTS_PATH, 'r') as file:
            linhas = file.readlines()
        with open(HOSTS_PATH, 'w') as file:
            for linha in linhas:
                if url not in linha:
                    file.write(linha)
        messagebox.showinfo("Sucesso", f"Site desbloqueado: {url}")
    except PermissionError:
        messagebox.showerror("Permissão negada", "Execute o programa como administrador/root.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Criando a interface
janela = tk.Tk()
janela.title("Bloqueador de Sites")
janela.geometry("400x200")
janela.resizable(False, False)

fonte = ("Arial", 12)

tk.Label(janela, text="Digite o site (ex: www.facebook.com):", font=fonte).pack(pady=10)

entrada = tk.Entry(janela, width=40, font=fonte)
entrada.pack(pady=5)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)

btn_bloquear = tk.Button(frame_botoes, text="Bloquear", command=bloquear_site, width=15, font=fonte, bg="red", fg="white")
btn_bloquear.grid(row=0, column=0, padx=10)

btn_desbloquear = tk.Button(frame_botoes, text="Desbloquear", command=desbloquear_site, width=15, font=fonte, bg="green", fg="white")
btn_desbloquear.grid(row=0, column=1, padx=10)

janela.mainloop()
