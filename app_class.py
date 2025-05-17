import datetime
from customtkinter import (CTk, CTkLabel, CTkOptionMenu, CTkEntry, CTkButton, 
                          CTkFrame, CTkCheckBox)
from tkinter import messagebox
from database import DatabaseManager
import re
import pandas as pd
import os
from tkinter import filedialog
import sqlite3

class App(CTk):
    def __init__(self, 
                 titulo="Sistema de Empréstimo de Equipamentos",
                 equipamentos=["Equipamento", "Lapela", "Chromebook", "Caixa de Som"]):
        
        super().__init__()
        self.title(titulo)
        self.geometry("400x600")  # Aumentei a altura para caber o novo botão
        self.minsize(400, 600)
        
        # Initialize database manager
        self.db_manager = DatabaseManager()
        
        self.grid_columnconfigure(0, weight=1)

        # UI Elements
        self._create_widgets(equipamentos)
        self._setup_layout()
        
    def _create_widgets(self, equipamentos):
        # Current date and time
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        current_time = datetime.datetime.now().strftime("%H:%M")
        
        # Main widgets
        self.apptitle = CTkLabel(self, text="Sistema de Empréstimo", font=("Arial", 16, "bold"))
        
        self.data_entry = CTkEntry(self, placeholder_text="Data", width=120)
        self.data_entry.insert(0, current_date)
        
        # Equipment frame
        self.equipamento_frame = CTkFrame(self, fg_color="transparent", border_width=2, 
                                        border_color="#444444", height=36)
        self.equipamento = CTkOptionMenu(
            self.equipamento_frame, 
            values=equipamentos, 
            fg_color="#222222",
            button_color="#444444",
            button_hover_color="#000000",
            text_color="white"
        )
        self.equipamento.pack(fill="x", padx=2, pady=2)
        
        self.patrimonio_entry = CTkEntry(self, placeholder_text="Patrimônio")
        self.nome_entry = CTkEntry(self, placeholder_text="Nome do Solicitante")
        self.matricula_entry = CTkEntry(self, placeholder_text="Matrícula")
        self.telefone_entry = CTkEntry(self, placeholder_text="Telefone")

        # Frame para sala (simplificado para um único campo de entrada)
        self.sala_frame = CTkFrame(self, fg_color="transparent", border_width=2, border_color="#444444", height=36)
        self.sala_entry = CTkEntry(self.sala_frame, placeholder_text="Digite o nome da sala")
        self.sala_entry.pack(fill="x", padx=2, pady=2)
        
        self.hora_emprestimo_entry = CTkEntry(self, placeholder_text="Hora do Empréstimo", width=120)
        self.hora_emprestimo_entry.insert(0, current_time)
        
        self.hora_devolucao_entry = CTkEntry(self, placeholder_text="Hora da Devolução", width=120)
        self.hora_devolucao_entry.insert(0, current_time)
        
        self.check_devolvido = CTkCheckBox(self, text="Devolvido")
        
        self.enviar_button = CTkButton(self, text="Enviar", command=self.enviar)
        self.limpar_button = CTkButton(self, text="Limpar", command=self.limpar_campos, 
                                      fg_color="transparent", border_width=1, 
                                      text_color=("black", "white"))
        
        # Novo botão para exportar para Excel
        self.exportar_button = CTkButton(
            self, 
            text="Exportar para Excel", 
            command=self.exportar_para_excel,
            fg_color="#2e8b57",  # Verde
            hover_color="#3cb371"
        )
        
    def _setup_layout(self):
        # Grid layout configuration
        rows = [
            (self.apptitle, 0),
            (self.data_entry, 1),
            (self.equipamento_frame, 2),
            (self.patrimonio_entry, 3),
            (self.nome_entry, 4),
            (self.matricula_entry, 5),
            (self.telefone_entry, 6),
            (self.sala_frame, 7),  # Frame da sala simplificado
            (self.hora_emprestimo_entry, 8),
            (self.hora_devolucao_entry, 9),
            (self.check_devolvido, 10),
            (self.enviar_button, 11),
            (self.limpar_button, 12),
            (self.exportar_button, 13)  # Ajustado para nova posição
        ]
        
        for widget, row in rows:
            widget.grid(row=row, column=0, pady=(4, 4), padx=10, sticky="ew")
    
    def _validate_inputs(self):
        required_fields = [
            (self.equipamento.get(), "Equipamento", "Selecione um equipamento"),
            (self.patrimonio_entry.get(), "Patrimônio", "Informe o número do patrimônio"),
            (self.nome_entry.get(), "Nome", "Informe o nome do solicitante"),
            (self.matricula_entry.get(), "Matrícula", "Informe a matrícula"),
            (self.sala_entry.get(), "Sala", "Informe o nome da sala")
        ]
        
        for value, field_name, error_msg in required_fields:
            if not value or value == field_name:
                messagebox.showwarning("Campo obrigatório", error_msg)
                return False
        
        # Validate phone number format (optional)
        telefone = self.telefone_entry.get()
        if telefone and not re.match(r'^\(\d{2}\) \d{4,5}-\d{4}$', telefone):
            if not messagebox.askyesno(
                "Formato de telefone",
                "Telefone não está no formato padrão (XX) XXXX-XXXX. Deseja continuar?"
            ):
                return False
        
        return True
    
    def enviar(self):
        if not self._validate_inputs():
            return
        
        dados = {
            "data": self.data_entry.get(),
            "equipamento": self.equipamento.get(),
            "patrimonio": self.patrimonio_entry.get(),
            "nome_solicitante": self.nome_entry.get(),
            "matricula": self.matricula_entry.get(),
            "telefone": self.telefone_entry.get(),
            "sala": self.sala_entry.get(),  # Usando o campo direto da entrada
            "hora_emprestimo": self.hora_emprestimo_entry.get(),
            "hora_devolucao": self.hora_devolucao_entry.get(),
            "devolvido": 1 if self.check_devolvido.get() else 0
        }
        
        if self.db_manager.save_loan(dados):
            messagebox.showinfo("Sucesso", "Empréstimo registrado com sucesso!")
            self.limpar_campos()
    
    def limpar_campos(self):
        # Clear all fields
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        current_time = datetime.datetime.now().strftime("%H:%M")
        
        self.data_entry.delete(0, 'end')
        self.data_entry.insert(0, current_date)
        self.equipamento.set("Equipamento")
        self.patrimonio_entry.delete(0, 'end')
        self.nome_entry.delete(0, 'end')
        self.matricula_entry.delete(0, 'end')
        self.telefone_entry.delete(0, 'end')
        self.sala_entry.delete(0, 'end')
        self.hora_emprestimo_entry.delete(0, 'end')
        self.hora_emprestimo_entry.insert(0, current_time)
        self.hora_devolucao_entry.delete(0, 'end')
        self.hora_devolucao_entry.insert(0, current_time)
        self.check_devolvido.deselect()
    
    def exportar_para_excel(self):
        try:
            # Obter todos os empréstimos do banco de dados
            conn = sqlite3.connect('emprestimos.db')
            query = "SELECT * FROM emprestimos"
            df = pd.read_sql_query(query, conn)
            conn.close()
            
            if df.empty:
                messagebox.showwarning("Sem dados", "Não há dados para exportar.")
                return
            
            # Converter coluna 'devolvido' para texto mais legível
            df['devolvido'] = df['devolvido'].map({1: 'Sim', 0: 'Não'})
            
            # Ordenar por data (mais recente primeiro)
            df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
            df = df.sort_values('data', ascending=False)
            df['data'] = df['data'].dt.strftime('%d/%m/%Y')
            
            # Pedir ao usuário onde salvar o arquivo
            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Arquivos Excel", "*.xlsx"), ("Todos os arquivos", "*.*")],
                title="Salvar como",
                initialfile="emprestimos_equipamentos.xlsx"
            )
            
            if not file_path:  # Usuário cancelou
                return
                
            # Exportar para Excel
            df.to_excel(file_path, index=False, engine='openpyxl')
            
            # Abrir o arquivo no Excel
            try:
                os.startfile(file_path)  # Para Windows
            except:
                messagebox.showinfo(
                    "Exportação concluída", 
                    f"Dados exportados com sucesso para:\n{file_path}\n\n"
                    "O arquivo foi salvo, mas não foi possível abri-lo automaticamente."
                )
            else:
                messagebox.showinfo(
                    "Exportação concluída", 
                    f"Dados exportados com sucesso para:\n{file_path}\n\n"
                    "O arquivo foi aberto no Microsoft Excel."
                )
                
        except Exception as e:
            messagebox.showerror("Erro na exportação", f"Ocorreu um erro ao exportar os dados:\n{str(e)}")


if __name__ == "__main__":
    app = App()
    app.mainloop()