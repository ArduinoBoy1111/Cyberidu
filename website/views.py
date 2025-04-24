from flask import Blueprint ,render_template ,request
import os

views = Blueprint('views', __name__)

@views.route('/')
def home():
    projects = [
    {
        "name": "حساس الطقس",
        "image": "arduino_project1.png",
        "price": 49.99,
        "description": "حساس لقياس درجة الحرارة والرطوبة",
        "new": True
    },
    {
        "name": "المنزل الذكي",
        "image": "arduino_project2.jpg",
        "price": 89.99,
        "description": "نظام أمان منزلي ذكي مع كاميرا مراقبة"
    },
    {
        "name": "ذراع روبوتية",
        "image": "arduino_project3.jpg",
        "price": 129.99,
        "description": "ذراع روبوتية قابلة للبرمجة للتحكم عن بعد",
        "new": True
    },
    {
        "name": "مشروع تجريبي 1",
        "image": "test_image.png",
        "price": 15.00,
        "description": "وصف افتراضي لمشروع تجريبي لغرض الاختبار",
        "new": False
    },
    {
        "name": "مشروع جديد 2",
        "image": "test_image.png",
        "price": 25.50,
        "description": "مشروع تجريبي مع علامة جديد",
        "new": True
    },
    {
        "name": "نظام مراقبة",
        "image": "test_image.png",
        "price": 60.00,
        "description": "نظام تجريبي لمراقبة البيئة الداخلية",
        "new": False
    },
    {
        "name": "تطبيق مدرسي",
        "image": "test_image.png",
        "price": 40.00,
        "description": "تطبيق بسيط لتجربة عرض المشاريع",
        "new": True
    }
    ]
    return render_template("base.html",projects=projects)

@views.route('/about')
def about():
    return render_template("about.html")


@views.route('/arduino_projects')
def arduino_projects():
    projects = [
        {
            "name": "حساس الطقس",
            "image": "arduino_project1.png",
            "price": 49.99,
            "description": "حساس لقياس درجة الحرارة والرطوبة"
        },
        {
            "name": "المنزل الذكي",
            "image": "arduino_project2.jpg",
            "price": 89.99,
            "description": "نظام أمان منزلي ذكي مع كاميرا مراقبة"
        },
        {
            "name": "ذراع روبوتية",
            "image": "arduino_project3.jpg",
            "price": 129.99,
            "description": "ذراع روبوتية قابلة للبرمجة للتحكم عن بعد"
        }
    ]
    return render_template("arduino_page.html",projects=projects)

@views.route('/project/<project_name>')
def project(project_name):
    # In a real app, you would look up these details from a database
    # For now, we'll get them from query parameters
    project_image = request.args.get('image')
    project_price = request.args.get('price')
    project_description = request.args.get('description')
    
    return render_template("project.html",
                        project_name=project_name,
                        project_image=project_image,
                        project_price=project_price,
                        project_description=project_description)
@views.route('/software_projects')
def software_projects():
    return render_template("software_page.html")