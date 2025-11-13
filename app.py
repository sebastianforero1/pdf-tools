import streamlit as st
from pypdf import PdfReader, PdfWriter
from pdf2docx import Converter
import io
import tempfile
import os

st.set_page_config(page_title="PDF Tools", layout="wide", page_icon="📄")

st.title("🔧 PDF Tools - Local")
st.markdown("---")

menu = st.sidebar.selectbox(
    "Herramienta",
    ["🔗 Fusionar PDFs", "✂️ Dividir PDF", "📄 PDF a Word", "🔄 Rotar", "🗑️ Eliminar Páginas"]
)

# FUSIONAR
if menu == "🔗 Fusionar PDFs":
    st.header("Fusionar PDFs")
    files = st.file_uploader("Sube PDFs", type=['pdf'], accept_multiple_files=True)
    
    if files and st.button("Fusionar"):
        writer = PdfWriter()
        for f in files:
            reader = PdfReader(f)
            for page in reader.pages:
                writer.add_page(page)
        
        output = io.BytesIO()
        writer.write(output)
        output.seek(0)
        
        st.download_button("📥 Descargar", output, "fusionado.pdf", "application/pdf")

# DIVIDIR
elif menu == "✂️ Dividir PDF":
    st.header("Dividir PDF")
    file = st.file_uploader("Sube PDF", type=['pdf'])
    
    if file:
        reader = PdfReader(file)
        total = len(reader.pages)
        st.info(f"Total: {total} páginas")
        
        start = st.number_input("Desde", 1, total, 1)
        end = st.number_input("Hasta", 1, total, total)
        
        if st.button("Extraer"):
            writer = PdfWriter()
            for i in range(start - 1, end):
                writer.add_page(reader.pages[i])
            
            output = io.BytesIO()
            writer.write(output)
            output.seek(0)
            
            st.download_button("📥 Descargar", output, f"pag_{start}_{end}.pdf", "application/pdf")

# PDF A WORD
elif menu == "📄 PDF a Word":
    st.header("PDF → Word")
    file = st.file_uploader("Sube PDF", type=['pdf'])
    
    if file and st.button("Convertir"):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_pdf:
            tmp_pdf.write(file.read())
            tmp_pdf_path = tmp_pdf.name
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp_docx:
            tmp_docx_path = tmp_docx.name
        
        cv = Converter(tmp_pdf_path)
        cv.convert(tmp_docx_path)
        cv.close()
        
        with open(tmp_docx_path, 'rb') as f:
            docx_bytes = f.read()
        
        os.unlink(tmp_pdf_path)
        os.unlink(tmp_docx_path)
        
        st.download_button("📥 Descargar", docx_bytes, "convertido.docx",
                          "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

# ROTAR
elif menu == "🔄 Rotar":
    st.header("Rotar Páginas")
    file = st.file_uploader("Sube PDF", type=['pdf'])
    
    if file:
        reader = PdfReader(file)
        angle = st.selectbox("Ángulo", [90, 180, 270])
        
        if st.button("Rotar todas"):
            writer = PdfWriter()
            for page in reader.pages:
                page.rotate(angle)
                writer.add_page(page)
            
            output = io.BytesIO()
            writer.write(output)
            output.seek(0)
            
            st.download_button("📥 Descargar", output, "rotado.pdf", "application/pdf")

# ELIMINAR
elif menu == "🗑️ Eliminar Páginas":
    st.header("Eliminar Páginas")
    file = st.file_uploader("Sube PDF", type=['pdf'])
    
    if file:
        reader = PdfReader(file)
        total = len(reader.pages)
        st.info(f"Total: {total} páginas")
        
        to_delete = st.text_input("Páginas a eliminar (ej: 2,4,6)")
        
        if to_delete and st.button("Eliminar"):
            delete_list = [int(x.strip()) for x in to_delete.split(',')]
            writer = PdfWriter()
            
            for i in range(total):
                if (i + 1) not in delete_list:
                    writer.add_page(reader.pages[i])
            
            output = io.BytesIO()
            writer.write(output)
            output.seek(0)
            
            st.download_button("📥 Descargar", output, "editado.pdf", "application/pdf")

st.markdown("---")
st.markdown("🔒 **100% Local** - Sin servidores externos")
