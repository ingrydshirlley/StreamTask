import streamlit as st
from database import create_tables
from database import add_task, get_tasks, mark_done, delete_task


create_tables()

st.set_page_config(page_title="Task Manager", layout="centered")

st.title("📝 Task Manager")

# Adicionar tarefa
task = st.text_input("Nova tarefa:")

if st.button("Adicionar"):
    if task:
        add_task(task)
        st.success("Tarefa adicionada com sucesso!")
        st.rerun()


# Listar tarefas
st.subheader("📋 Tarefas")
tasks = get_tasks()
for task_id, description, done in tasks:
    if not done:
        col1, col2 = st.columns([0.8, 0.2])  # Dividir linha em checkbox + botão
        with col1:
            if st.checkbox(description, key=task_id):
                mark_done(task_id)
                st.rerun()
        with col2:
            if st.button("🗑️", key=f"del_{task_id}"):
                delete_task(task_id)
                st.rerun()


# Mostrar tarefas concluídas
with st.expander("✅ Concluídas"):
    for task_id, description, done in tasks:
        if done:
            st.write(f"✔️ {description}")
