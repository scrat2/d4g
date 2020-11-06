function creationPDF() {
            var doc = new jsPDF('l', 'cm', 'a3');

            doc.setProperties({
             title: 'Résultat de la recherche',
             subject: 'Indice de fragilité numérique',
             author: 'Equipe 21',
             keywords: 'generated, javascript, web 2.0, ajax',
            });

            doc.margins = {top: 2, bottom: 2, left: 2, right: 2};

            doc.setFontSize(9);
            doc.setFont("arial", "normal");
            doc.text('Ce PDF est généré depuis de site web http://vps-66b01329.vps.ovh.net/, sujet : indice de fragilité numérique, auteur : Equipe 21, contexte: Design4Green', 2, 2);

            doc.setLineWidth(0.1);
            doc.line(1,3,41,3);

            doc.setFontSize(20);
            doc.setFont("arial", "bold");
            doc.text('Résultat de la recherche :', 2, 5);

            var source = window.document.getElementsByClassName("resultats")[0];
            doc.fromHTML(source, 2,6,{'witdh':20});

            doc.save('ResultatRecherche.pdf');
        }
