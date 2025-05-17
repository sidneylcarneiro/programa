import sqlite3
from tkinter import messagebox

class DatabaseManager:
    def __init__(self, db_name='emprestimos.db'):
        self.db_name = db_name
        self._create_table()
    
    def _create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS emprestimos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT,
                    equipamento TEXT,
                    patrimonio TEXT,
                    nome_solicitante TEXT,
                    matricula TEXT,
                    telefone TEXT,
                    sala TEXT,
                    hora_emprestimo TEXT,
                    hora_devolucao TEXT,
                    devolvido INTEGER
                )
            ''')
            conn.commit()
    
    def save_loan(self, loan_data):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO emprestimos (
                        data, equipamento, patrimonio, nome_solicitante, 
                        matricula, telefone, sala, hora_emprestimo, 
                        hora_devolucao, devolvido
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    loan_data["data"],
                    loan_data["equipamento"],
                    loan_data["patrimonio"],
                    loan_data["nome_solicitante"],
                    loan_data["matricula"],
                    loan_data["telefone"],
                    loan_data["sala"],
                    loan_data["hora_emprestimo"],
                    loan_data["hora_devolucao"],
                    loan_data["devolvido"]
                ))
                conn.commit()
                return True
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            return False

