function creationPDF() {
            var doc = new jsPDF();
            doc.text(10, 10, 'hello woldr');
            doc.save('ResultatRecherche.pdf');
        }