let populate = function() {
    let team1 = document.getElementById('team-1');
    let team2 = document.getElementById('team-2');
    let countries = [
        {value: " Afghanistan " , text: " Afghanistan " },
        {value: " Australia ", text: " Australia "},
        {value: " Bangladesh ", text: " Bangladesh "},
        {value: " Bermuda ", text: " Bermuda "},
        {value: " Canada ", text: " Canada "},
        {value: " East Africa ", text: " East Africa "},
        {value: " England ", text: " England "},
        {value: " Hong Kong ", text: " Hong Kong "},
        {value: " India ", text: " India "},
        {value: " Ireland ", text: " Ireland "},
        {value: " Kenya ", text: " Kenya "},
        {value: " Namibia ", text: " Namibia "},
        {value: " Netherlands ", text: " Netherlands "},
        {value: " New Zealand ", text: " New Zealand "},
        {value: " P.N.G. ", text: " P.N.G. "},
        {value: " Pakistan ", text: " Pakistan "},
        {value: " Scotland ", text: " Scotland "},
        {value: " South Africa ", text: " South Africa "},
        {value: " Sri Lanka ", text: " Sri Lanka "},
        {value: " U.A.E. ", text: " U.A.E. "},
        {value: " U.S.A. ", text: " U.S.A. "},
        {value: " West Indies ", text: " West Indies "},
        {value: " Zimbabwe ", text: " Zimbabwe "}
        ];
for(let i = 0; i< countries.length; i++){
    let option = document.createElement('option'); 
    option.setAttribute('value', countries[i].value);
    option.appendChild(document.createTextNode(countries[i].text));
    team1.appendChild(option);

}
for(let i = 0; i< countries.length; i++){
    let option = document.createElement('option'); 
    option.setAttribute('value', countries[i].value);
    option.appendChild(document.createTextNode(countries[i].text));
    team2.appendChild(option);

}

}

window.onload = populate();