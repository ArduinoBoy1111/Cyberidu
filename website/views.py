from flask import Blueprint, render_template, request

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
        }
    ]
    return render_template("base.html", projects=projects)

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
    return render_template("arduino_page.html", projects=projects)

@views.route('/software_projects')
def software_projects():
    projects = [
        {
            "name": "تطبيق مدرسي",
            "image": "test_image.png",
            "price": 40.00,
            "description": "تطبيق بسيط لتجربة عرض المشاريع"
        },
        {
            "name": "مشروع تجريبي 1",
            "image": "test_image.png",
            "price": 15.00,
            "description": "وصف افتراضي لمشروع تجريبي لغرض الاختبار"
        }
    ]
    return render_template("software_page.html", projects=projects)

@views.route('/project/<project_name>')
def project(project_name):
    # This one supports a list of images
    all_projects = [
        {
            "name": "حساس الطقس",
            "images": ["arduino_project1.png", "arduino_project2.jpg"],
            "price": 49.99,
            "description": "حساس لقياس درجة الحرارة والرطوبة"
        },
        {
            "name": "المنزل الذكي",
            "images": ["arduino_project2.jpg", "arduino_project2_alt.jpg"],
            "price": 89.99,
            "description": "نظام أمان منزلي ذكي مع كاميرا مراقبة"
        },
        {
            "name": "ذراع روبوتية",
            "images": ["arduino_project3.jpg", "arduino_project3_alt.jpg"],
            "price": 129.99,
            "description": "ذراع روبوتية قابلة للبرمجة للتحكم عن بعد"
        },
        {
            "name": "مشروع تجريبي 1",
            "images": ["test_image.png"],
            "price": 15.00,
            "description": "وصف افتراضي لمشروع تجريبي لغرض الاختبار"
        },
        {
            "name": "مشروع جديد 2",
            "images": ["test_image.png"],
            "price": 25.50,
            "description": "مشروع تجريبي مع علامة جديد"
        },
        {
            "name": "نظام مراقبة",
            "images": ["test_image.png"],
            "price": 60.00,
            "description": "نظام تجريبي لمراقبة البيئة الداخلية"
        },
        {
            "name": "تطبيق مدرسي",
            "images": ["test_image.png"],
            "price": 40.00,
            "description": "تطبيق بسيط لتجربة عرض المشاريع"
        }
    ]

    project = next((p for p in all_projects if p["name"] == project_name), None)

    if not project:
        return "المشروع غير موجود", 404

    return render_template(
        "project.html",
        project_name=project["name"],
        project_images=project["images"],
        project_price=project["price"],
        project_description=project["description"]
    )
