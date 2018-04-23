define(function(){

    function _on_load(){
          IPython.notebook.kernel.execute("URL = '" + window.location + "'"); 
    }

    return {load_ipython_extension: _on_load };
})

