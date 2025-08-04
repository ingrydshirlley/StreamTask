import streamlit as st
from database import create_tables
from database import add_task, get_tasks, mark_done, delete_task


create_tables()

st.set_page_config(page_title="Task Manager", layout="centered")

st.title("📝 Task Manager")

# Adicionar tarefa
col1, col2 = st.columns([4, 1])  # Coluna maior pro input, menor pro botão

with col1:
    task = st.text_input('default')

with col2:
    if st.button("Adicionar"):
        if task:
            add_task(task)
            st.success("Tarefa adicionada com sucesso!")
            st.rerun()

# Espaço para um espaçamento mais harmônico
st.write("")
st.write("")
st.write("")
st.write("")

# Listar tarefas
st.subheader("📋 Tarefas")
tasks = get_tasks()
for task_id, description, done in tasks:
    if not done:
        col3, col4 = st.columns([0.8, 0.2])  # Dividir linha em checkbox + botão
        with col3:
            if st.checkbox(description, key=task_id):
                mark_done(task_id)
                st.rerun()
        with col4:
            if st.button("🗑️", key=f"del_{task_id}"):
                delete_task(task_id)
                st.rerun()


# Mostrar tarefas concluídas
with st.expander("✅ Concluídas"):
    for task_id, description, done in tasks:
        if done:
            st.write(f"✔️ {description}")
