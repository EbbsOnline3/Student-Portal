import os
from flask import Flask, jsonify, render_template, request, flash, current_app
import json
import mysql.connector
from mysql.connector import Error



app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_CODE', 'secret')

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user=os.environ.get('DB_USER', 'root'),          
        password=os.environ.get('DB_PASSWORD'),  
        database=os.environ.get('DB_NAME')
    )


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

districts_by_region = {
    "greater accra": [
        "Accra Metropolitan", "Tema Metropolitan", "Adenta Municipal",
        "Ashaiman Municipal", "Ga Central Municipal", "Ga East Municipal",
        "Ga North Municipal", "Ga South Municipal", "Ga West Municipal",
        "Kpone-Katamanso Municipal", "La Dade-Kotopon Municipal",
        "La Nkwantanang-Madina Municipal", "Ledzokuku Municipal",
        "Ningo-Prampram District", "Okaikwei North Municipal",
        "Shai-Osudoku District", "Tema West Municipal", "Weija-Gbawe Municipal",
        "Ablekuma Central Municipal", "Ablekuma North Municipal",
        "Ablekuma West Municipal", "Ayawaso Central Municipal",
        "Ayawaso East Municipal", "Ayawaso North Municipal",
        "Ayawaso West Municipal", "Korle Klottey Municipal", "Krowor Municipal"
    ],
    "central": [
        "Agona East", "Agona West Municipal", "Ajumako-Enyan-Essiam",
        "Asikuma-Odoben-Brakwa", "Assin Central Municipal", "Assin North",
        "Assin South", "Awutu Senya East Municipal", "Awutu Senya West",
        "Cape Coast Metropolitan", "Effutu Municipal", "Ekumfi", "Gomoa Central",
        "Gomoa East", "Gomoa West", "Komenda-Edina-Eguafo-Abirem Municipal",
        "Mfantseman Municipal", "Twifo-Ati Morkwa", "Twifo-Heman-Lower Denkyira",
        "Upper Denkyira East Municipal", "Upper Denkyira West"
    ],
    "western": [
        "Ahanta West", "Ellembelle", "Jomoro", "Kwesimintsim Municipal",
        "Mpohor", "Nzema East Municipal", "Prestea-Huni Valley Municipal",
        "Sekondi-Takoradi Metropolitan", "Shama", "Tarkwa-Nsuaem Municipal",
        "Wassa Amenfi Central", "Wassa Amenfi East", "Wassa Amenfi West"
    ],
    "western north": [
        "Aowin Municipal", "Bia East", "Bia West", "Bibiani-Anhwiaso-Bekwai Municipal",
        "Bodi", "Juaboso", "Sefwi-Akontombra", "Sefwi-Wiawso Municipal", "Suaman"
    ],
    "volta": [
        "Adaklu", "Afadzato South", "Agotime-Ziope", "Akatsi North",
        "Akatsi South", "Anloga", "Central Tongu", "Ho Municipal", "Ho West",
        "Hohoe Municipal", "Keta Municipal", "Ketu North Municipal",
        "Ketu South Municipal", "Kpando Municipal", "North Dayi", "North Tongu",
        "South Dayi", "South Tongu"
    ],
    "oti": [
        "Biakoye", "Jasikan", "Kadjebi", "Krachi East Municipal",
        "Krachi Nchumuru", "Krachi West", "Nkwanta North", "Nkwanta South Municipal"
    ],
    "eastern": [
        "Abuakwa North Municipal", "Abuakwa South Municipal", "Achiase",
        "Akropong", "Akuapim North Municipal", "Akuapim South", "Akyemansa",
        "Asene Manso Akroso", "Asuogyaman", "Atiwa East", "Atiwa West",
        "Ayensuano", "Birim Central Municipal", "Birim North", "Birim South",
        "Denkyembour", "Fanteakwa North", "Fanteakwa South", "Kwaebibirem Municipal",
        "Kwahu Afram Plains North", "Kwahu Afram Plains South", "Kwahu East",
        "Kwahu South", "Kwahu West Municipal", "Lower Manya Krobo Municipal",
        "New-Juaben North Municipal", "New-Juaben South Municipal",
        "Nsawam-Adoagyiri Municipal", "Okere", "Suhum Municipal",
        "Upper Manya Krobo", "Yilo Krobo Municipal"
    ],
    "ashanti": [
        "Adansi Asokwa", "Adansi North", "Adansi South", "Afigya Kwabre North",
        "Afigya Kwabre South", "Ahafo Ano North", "Ahafo Ano South East",
        "Ahafo Ano South West", "Akrofuom", "Amansie Central", "Amansie South",
        "Amansie West", "Asante Akim Central Municipal", "Asante Akim North Municipal",
        "Asante Akim South", "Asokore Mampong Municipal", "Asokwa Municipal",
        "Atwima Kwanwoma", "Atwima Mponua", "Atwima Nwabiagya North",
        "Atwima Nwabiagya South", "Bekwai Municipal", "Bosome Freho", "Bosomtwe",
        "Ejisu Municipal", "Ejura-Sekyedumase Municipal", "Juaben Municipal",
        "Kwabre East Municipal", "Kwadaso Municipal", "Mampong Municipal",
        "Obuasi East", "Obuasi Municipal", "Offinso North", "Offinso South Municipal",
        "Oforikrom Municipal", "Old Tafo Municipal", "Suame Municipal"
    ],
    "bono": [
        "Banda", "Berekum East Municipal", "Berekum West", "Dormaa Central Municipal",
        "Dormaa East", "Dormaa West", "Jaman North", "Jaman South Municipal",
        "Sunyani Municipal", "Sunyani West", "Tain", "Wenchi Municipal"
    ],
    "bono east": [
        "Atebubu-Amantin Municipal", "Kintampo North Municipal", "Kintampo South",
        "Nkoranza North", "Nkoranza South Municipal", "Pru East", "Pru West",
        "Sene East", "Sene West", "Techiman Municipal", "Techiman North"
    ],
    "ahafo": [
        "Asunafo North Municipal", "Asunafo South", "Asutifi North", "Asutifi South",
        "Tano North Municipal", "Tano South Municipal"
    ],
    "northern": [
        "Kumbungu", "Mion", "Nanton", "Nanumba North Municipal", "Nanumba South",
        "Saboba", "Sagnarigu Municipal", "Savelugu Municipal", "Tamale Metropolitan",
        "Tatale-Sanguli", "Tolon", "Yendi Municipal", "Zabzugu"
    ],
    "savannah": [
        "Bole", "Central Gonja", "Daboya-Mankarigu", "Damongo", "East Gonja Municipal",
        "Kpandai", "North Gonja", "Sawla-Tuna-Kalba", "West Gonja Municipal"
    ],
    "north east": [
        "Bunkpurugu-Nakpanduri", "Chereponi", "East Mamprusi Municipal",
        "Mamprugu-Moagduri", "West Mamprusi Municipal", "Yunyoo-Nasuan"
    ],
    "upper east": [
        "Bawku Municipal", "Bawku West", "Binduri", "Bolgatanga East",
        "Bolgatanga Municipal", "Bongo", "Builsa North Municipal", "Builsa South",
        "Garu", "Kassena-Nankana East Municipal", "Kassena-Nankana West",
        "Nabdam", "Pusiga", "Talensi", "Tempane"
    ],
    "upper west": [
        "Daffiama-Bussie-Issa", "Jirapa Municipal", "Lambussie Karni",
        "Lawra Municipal", "Nadowli-Kaleo", "Nandom Municipal",
        "Sissala East Municipal", "Sissala West", "Wa East", "Wa Municipal", "Wa West"
    ]
}

# list of region names (keys)
regions = list(districts_by_region.keys())

@app.route('/getstarted', methods = ['GET', 'POST'])
def get_started():
    return render_template('getstarted.html', districts_by_region = districts_by_region, regions = regions)


@app.route('/getstarted/register', methods = ['POST'])
def register():
    try:
        req = request.get_json()
        
        
        firstName = req['firstName']
        middleName = req.get('middleName')
        lastName = req['lastName']
        email = req['email'].strip().lower()
        dateOfBirth = req['dateOfBirth']
        address = req['address']
        gender = req['gender']
        phone = req['phoneNumber']
        region = req['region']
        district = req['district']
        nextOfKin = req['nextOfKin']
        academicScore = req['academicScore']
        
        if firstName == '' | lastName == '':
            flash('Fields cannot be empty', 'flash_error')
            return

        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO student_info 
            (first_name, middle_name, last_name, email, date_of_birth, address, 
             gender, phone_number, region, district, next_of_kin, wassce_score, profile_image_path)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            firstName, middleName, lastName, email, dateOfBirth,
            address, gender, phone, region, district, nextOfKin, academicScore
        )

        cursor.execute(sql, values)
        conn.commit()
        new_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return jsonify({
            'success': True,
            'message': 'Student registered successfully!',
            'student_id': new_id
        })

    except mysql.connector.Error as e:
        if e.errno == 1062:  # Duplicate email
            return jsonify({
                'success': False,
                'message': 'Email already registered.'
            }), 409
        return jsonify({
            'success': False,
            'message': f'Database error: {str(e)}'
        }), 500

    except KeyError as e:
        flash('Error')
        return jsonify({
            'success': False,
            'message': f'Missing field: {str(e)}'
        }), 400

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Server error: {str(e)}'
        }), 500

@app.route('/getstarted/student_detail', methods = ['GET','POST'])
def student_detail():
    return render_template('students.html')

@app.route('/getstarted/register/profile', methods = ['POST'])
def profile():
    profile_image = request.files['file']
    if profile_image:
        flash('Success')
    else:
        flash('Error')
    # profile_image_path = os.path.join(current_app.root_path, 'static/images') 
    # profile_image.save(profile_image_path)
    # print(profile_image_path)
    return jsonify({
            'success': True,
            'message': 'Student registered successfully!',
        })


if __name__ == '__main__':
    app.run(debug=True)
