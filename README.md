# 📦 Sistema de Inventario en Django  

**Evaluación N°2 – Programación Back End**  
**Alumno:** Mauricio Toloza  

---

## 🚀 Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:  

- [Python 3.11+](https://www.python.org/)
- [Django 5.x](https://www.djangoproject.com/)  
- [MySQL Server + Workbench](https://dev.mysql.com/downloads/)  
- [Django REST Framework](https://www.django-rest-framework.org/)  

Librerías necesarias:  

```bash
pip install django djangorestframework mysqlclient
```

Si `mysqlclient` falla en Windows, puedes usar:  

```bash
pip install pymysql
```

y en el archivo `__init__.py` del proyecto:  

```py
import pymysql
pymysql.install_as_MySQLdb()
```

---

## ⚙️ Configuración de la Base de Datos

1. Ingresar a MySQL y crear la base de datos y usuario:  

```sql
CREATE DATABASE inventario_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'django_user'@'localhost' IDENTIFIED BY 'clave123';
GRANT ALL PRIVILEGES ON inventario_db.* TO 'django_user'@'localhost';
FLUSH PRIVILEGES;
```

1. En `settings.py` configurar:  

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inventario_db',
        'USER': 'django_user',
        'PASSWORD': 'clave123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

1. Aplicar migraciones:  

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🛠️ Modelos Implementados

El sistema tiene **5 apps** en Django, cada una con su propio modelo:  

- **categorias** → `Categoria`  
- **proveedores** → `Proveedor`  
- **bodegas** → `Bodega`  
- **productos** → `Producto`  
- **movimientos** → `Movimiento`  

Relaciones principales:  

- Un **producto** pertenece a una categoría y a un proveedor.  
- Un **movimiento** está asociado a un producto y a una bodega.  
- Los movimientos afectan el `stock_actual` del producto.  

---

## 🖥️ Uso del Administrador de Django

1. Crear superusuario:  

```bash
python manage.py createsuperuser
```

1. Ingresar en:  

``` url
http://127.0.0.1:8000/admin/
```

1. En el admin se registraron todos los modelos.  
   - **Producto** fue personalizado con:
     - `list_display` (muestra columnas adicionales)  
     - `search_fields` (búsqueda por nombre/sku)  
     - `list_filter` (filtro por categoría y proveedor)  

---

## 🔗 Endpoints Disponibles

El sistema expone endpoints con **Django REST Framework**:  

- `/categorias/`  
- `/proveedores/`  
- `/bodegas/`  
- `/productos/`  
- `/movimientos/`  
- `/movimientos/historico/<id_producto>/` → histórico de movimientos de un producto.  

Cada endpoint soporta **CRUD completo** (listar, crear, editar, eliminar).  

---
