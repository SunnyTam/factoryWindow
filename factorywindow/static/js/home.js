/**
 * Created by Sunny on 3/6/2017.
 */

function onDdlSelected(selectedFabric, selectedClothing) {
    if(selectedFabric !== '' || selectedClothing !== '') {
        $('.pin').hide();
    } else {
        $('.pin').show();
    }
}

$(function () {
    $('.ui.dropdown').dropdown();

    var selectedFabric = '';
    var selectedClothing = '';

   $('.fabric-ddl').change(function(){
       selectedFabric = $(this).val();
       onDdlSelected(selectedFabric, selectedClothing);
   });

    $('.clothing-ddl').change(function(){
        selectedClothing = $(this).val();
        onDdlSelected(selectedFabric, selectedClothing);
   });
});