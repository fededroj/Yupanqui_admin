var $ = jQurty.noConflicy(); 

function abrir_modal_eliminar(url){
  $('#eliminar').load(url, function(){
$(this).modal('show');
  })
}