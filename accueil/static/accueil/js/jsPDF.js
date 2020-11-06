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

            var splitText = doc.splitTextToSize("La fragilité numérique est identifiée sur des critères liés à l'accès au numérique et sur le niveau de compétences de chacun et chacun.\n" +
                "L’indice de fragilité numérique des territoires a été produit dans le cadre de l’IncubO du SGAR Occitanie avec le concours de l’ANSA en partenariat avec la Mednum, grâce au soutien du Fond de transformation pour l’action publique.\n" +
                "L'indice de fragilité numérique, par sa représentation graphique, révèle les zones d'exclusion\n" +
                "numérique sur un territoire donné. Cet outil permet, que vous soyez une commune, un département\n" +
                "ou une région de comparer votre indice de fragilité numérique avec les autres territoires.", 250);

            doc.text(2, 5, splitText);

            doc.setFontSize(20);
            doc.setFont("arial", "bold");
            doc.text('Résultat de la recherche :', 2, 7.5);

            var source = window.document.getElementsByClassName("resultats")[0];
            doc.fromHTML(source, 2,8.5,{'witdh':50});

            doc.save('ResultatRecherche.pdf');
        }
