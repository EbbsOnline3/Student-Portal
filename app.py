from flask import Flask, render_template

app = Flask(__name__)

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



if __name__ == '__main__':
    app.run(debug=True)