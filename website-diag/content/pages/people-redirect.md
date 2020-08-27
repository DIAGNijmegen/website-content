title: Redirecting

This page has moved. You will be redirected.

<script type="text/javascript">

var valid_people = {"Bram_van_Ginneken": "bram-van-ginneken","Nico_Karssemeijer": "nico-karssemeijer","Francesco_Ciompi": "francesco-ciompi","Henkjan_Huisman": "henkjan-huisman","Colin_Jacobs": "colin-jacobs","Jeroen_van_der_Laak": "jeroen-van-der-laak","Geert_Litjens": "geert-litjens","Rashindra_Manniesing": "rashindra-manniesing","James_Meakin": "james-meakin","Matthieu_Rutten": "matthieu-rutten","Clarisa_S%C3%A1nchez": "clarisa-sanchez","Cornelia_Schaefer-Prokop": "cornelia-schaefer-prokop","Witali_Aswolinskiy": "witali-aswolinskiy","Thomas_van_den_Heuvel": "thomas-van-den-heuvel","Nikolas_Lessmann": "nikolas-lessmann","Caner_Mercan": "caner-mercan","Nikita_Moriakov": "nikita-moriakov","Keelin_Murphy": "keelin-murphy","Steven_Schalekamp": "steven-schalekamp","Ernst_Scholten": "ernst-scholten","Jonas_Teuwen": "jonas-teuwen","Elke_Loskamp-Huntink": "elke-loskamp-huntink","Rita_Bijlsma": "rita-bijlsma","Merijn_van_Erp": "merijn-van-erp","Paul_Konstantin_Gerke": "paul-konstantin-gerke","Miriam_Groeneveld": "miriam-groeneveld","Sjoerd_Kerkstra": "sjoerd-kerkstra","Sil_van_de_Leemput": "sil-van-de-leemput","Mike_Overkamp": "mike-overkamp","Maud_Wekking": "maud-wekking","Harm_van_Zeeland": "harm-van-zeeland","Alessandro_Ardu": "alessandro-ardu","Maschenka_Balkenhol": "maschenka-balkenhol","P%C3%A9ter_B%C3%A1ndi": "peter-bandi","Thomas_de_Bel": "thomas-de-bel","John-Melle_Bokhorst": "john-melle-bokhorst","Luuk_Boulogne": "luuk-boulogne","Patrick_Brand": "patrick-brand","Wouter_Bulten": "wouter-bulten","Erdi_Calli": "erdi-calli","Oscar_Debats": "oscar-debats","Koen_Dercksen": "koen-dercksen","Miguel_Fernandes": "miguel-fernandes","Daan_Geijs": "daan-geijs","Cristina_Gonzalez_Gonzalo": "cristina-gonzalez-gonzalo","Jasper_van_der_Graaf": "jasper-van-der-graaf","Tariq_Haddad": "tariq-haddad","Ward_Hendrix": "ward-hendrix","Meyke_Hermsen": "meyke-hermsen","Matin_Hosseinzadeh": "matin-hosseinzadeh","Gabriel_Humpire_Mamani": "gabriel-humpire-mamani","Michel_Kok": "michel-kok","Kevin_Koschmieder": "kevin-koschmieder","Kicky_van_Leeuwen": "kicky-van-leeuwen","Bart_Liefers": "bart-liefers","Jasper_Linmans": "jasper-linmans","Esther_Markus-Smeets": "esther-markus-smeets","Midas_Meijs": "midas-meijs","Ajay_Patel": "ajay-patel","Hans_Pinckaers": "hans-pinckaers","Sarah_van_Riel": "sarah-van-riel","Mart_van_Rijthoven": "mart-van-rijthoven","Riccardo_Samperna": "riccardo-samperna","Anton_Schreuder": "anton-schreuder","Cheryl_Sital": "cheryl-sital","Ecem_Sogancioglu": "ecem-sogancioglu","David_Tellez": "david-tellez","Kiran_Vaidhya_Venkadesh": "kiran-vaidhya-venkadesh","Coen_de_Vente": "coen-de-vente","Xie_Weiyi": "xie-weiyi","Gaby_Whitehead": "gaby-whitehead","Bram_de_Wilde": "bram-de-wilde","Ludo_van_Alst": "ludo-van-alst","Niels_van_den_Hork": "niels-van-den-hork","Thijs_van_den_Hout": "thijs-van-den-hout","Jeffrey_Hoven": "jeffrey-hoven","Ruben_Kluge": "ruben-kluge","Chase_Neff": "chase-neff","Martijn_Schilpzand": "martijn-schilpzand","Rens_van_Schouwenburg": "rens-van-schouwenburg","Grzegorz_Chlebus": "grzegorz-chlebus","Nils_Hendrix": "nils-hendrix","Alessa_Hering": "alessa-hering"
}

function getParameterByName(name, url) {
  if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

if(getParameterByName('name') in valid_people) {
    // Redirect to new people page
    window.location.replace(window.location.hostname + '/people/' + valid_people[getParameterByName('name')])
}
</script>