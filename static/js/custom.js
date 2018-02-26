function HideStud(){
    c = $('#twostud')[0].checked;
    works = $('#place_of_study')[0].children;

    jQuery.each(works, function() {
        hide = this.getAttribute('hide');
        if (hide == 'True' && c == true){
            this.classList.add('hidden');
        }
        else if (hide == 'True' && c == false){
            this.classList.remove('hidden');
        }
    });
}