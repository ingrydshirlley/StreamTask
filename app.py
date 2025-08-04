import streamlit as st
from database.database import create_tables
from ui.add_spacing import add_spacing
from database.database import add_task, get_tasks, mark_done, delete_task

create_tables()

st.set_page_config(page_title="Task Manager", layout="centered")
st.title("📝 Task Manager")


# Espaçamento 
add_spacing ()


# Adicionar tarefa
task = st.text_input('Nova tarefa:')
if st.button("Adicionar"):
    if task:
        add_task(task)
        st.success("Tarefa adicionada com sucesso!")
        st.rerun()
        
        
add_spacing ()


# Listar tarefas
st.subheader("📋 Tarefas")
tasks = get_tasks()
for task_id, description, done in tasks:
    if not done:
        col3, col4 = st.columns([0.8, 0.2]) 
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
