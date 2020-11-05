function creationPDF() {
            var doc = new jsPDF('p', 'cm', 'a4');
            var elementHandler = {
                '.ignorePDF':function (element, renderer) {
                    return true;
                }
            };
            var source = $("body")[0];

            doc.setProperties({
             title: 'Résultat de la recherche',
             subject: 'Indice de fragilité numérique',
             author: 'Team.Random() - Equipe 21',
             keywords: 'generated, javascript, web 2.0, ajax',
            });

            doc.margins = {top: 2, bottom: 2, left: 2, right: 2};

            doc.setFontSize(9);
            doc.setFont("arial", "normal");
            doc.text('Ce PDF est généré depuis de site web http://vps-66b01329.vps.ovh.net/, sujet : indice de fragilité numérique', 2, 2);
            doc.text('auteur : Team.Random() - Equipe 21, contexte: DesignGreen', 2, 2.5 );

            doc.setLineWidth(0.1);
            doc.line(1,3,20,3);

            doc.setFontSize(20);
            doc.setFont("arial", "bold");
            doc.text('Résultat de la recherche :', 2, 5);

            doc.fromHTML(source, 15,15,{'witdh':21, 'elementHandlers': elementHandler});

            doc.save('ResultatRecherche.pdf');
        }

$(document).ready(function () {
    creationPDF();
});