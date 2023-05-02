function showActiveLink(menu){
    try{
        const url = document.location.href
        const elem = document.getElementById(menu).querySelectorAll('a')
        for (const link of elem) {
            if(link.href===url){
                link.classList.add('active')
            }
        }
    }catch(e){
        console.log(e);
    }
}
showActiveLink('menu')