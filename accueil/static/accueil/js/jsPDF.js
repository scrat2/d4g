function creationPDF() {
            var doc = new jsPDF();
            doc.text(10, 10, 'hello world');
            doc.save('ResultatRecherche.pdf');
        }