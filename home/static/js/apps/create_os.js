/*Script destinado a dinamizar el comportamiento de las plantillas relacionadas
a la creación de una orden de servicio*/
var pasoVal = 1;
var subpasoVal = 1;
const lista_div = {
    paso2: ["paso_2_", "id_paso_2_", {
        sitio: ["paso_2_sitio_", "id_paso_2_sitio_"],
        servicio: ["paso_2_servicio_", "id_paso_2_servicio_"],
        }],
    paso3: ["paso_3_", "id_paso_3_"],
    paso4: ["paso_4_", "id_paso_4_"],
}

document.addEventListener('DOMContentLoaded', function() {
    iniciarApp();
})

function iniciarApp() {
    colapsar();
    pasosEstado();
    agregar_servicios();
    quitar_servicios();
    cerrarDiv();
}

function cerrarDiv() {
    const boton = document.getElementById("divCenter").querySelector(".cerrar");
    boton.addEventListener("click", event => {
        document.getElementById("divCenter").style.display = "none";
        document.querySelector("body").classList.remove("fijar-body");
    })
}

function agregar_servicios() {
    const boton_agregar = document.getElementById("id_agregar_servicio")
    boton_agregar.addEventListener('click', (e) => {
        let ss_total = document.getElementById("id_subservicios_total");
        const contenedor = document.getElementById("id_contenedor_sub_servicios");

        let div_servicio = document.createElement( "DIV" );
        div_servicio.setAttribute("name", "sub_servicio_content");
        div_servicio.setAttribute("id", "id_sub_servicio_content_" + ss_total.value);
        contenedor.appendChild(div_servicio);

        const button = document.createElement( "BUTTON" );
        button.innerHTML = `Servicio ${parseInt(ss_total.value) + 1}:`;
        button.classList.add('colapsar');
        button.type = "button";
        button.addEventListener("click", add_element);
        div_servicio.appendChild(button);

        const div_content = document.createElement( "DIV" );
        div_content.classList.add("content");
        div_content.classList.add("service-content");
        div_content.setAttribute('name', `sub_servicio_${ss_total.value}`);
        div_content.setAttribute('id', `id_sub_servicio_${ss_total.value}`);
        div_servicio.appendChild(div_content);

        const contenedor_paso_2 = document.createElement( "DIV" );
        contenedor_paso_2.classList.add("paso_2");
        contenedor_paso_2.setAttribute("id", "id_paso_2_" + ss_total.value);
        div_content.appendChild(contenedor_paso_2);
        
        const contenedor_instrumento = document.createElement( "DIV" );
        contenedor_instrumento.classList.add("paso_3_instrumento");
        contenedor_instrumento.setAttribute("id", "id_paso_3_instrumento_" + ss_total.value);
        div_content.appendChild(contenedor_instrumento);
        
        const contenedor_certificado = document.createElement( "DIV" );
        contenedor_certificado.classList.add("paso_3_certificado");
        contenedor_certificado.setAttribute("id", "id_paso_3_certificado_" + ss_total.value);
        div_content.appendChild(contenedor_certificado);
        
        const contenedor_facturacion = document.createElement( "DIV" );
        contenedor_facturacion.classList.add("paso_3_facturacion");
        contenedor_facturacion.setAttribute("id", "id_paso_3_facturacion_" + ss_total.value);
        div_content.appendChild(contenedor_facturacion);

        const contenedor_paso_4 = document.createElement( "DIV" );
        contenedor_paso_4.classList.add("paso_4");
        contenedor_paso_4.setAttribute("id", "id_paso_4_" + ss_total.value);
        div_content.appendChild(contenedor_paso_4);

        const contenedor_sitio = document.createElement( "DIV" );
        contenedor_sitio.setAttribute("id", "id_paso_2_sitio_" + ss_total.value);
        contenedor_paso_2.appendChild(contenedor_sitio);

        const contenedor_servicio = document.createElement( "DIV" );
        contenedor_servicio.setAttribute("id", "id_paso_2_servicio_" + ss_total.value);
        contenedor_paso_2.appendChild(contenedor_servicio);

        ss_total.value = parseInt(ss_total.value) + 1;
        document.getElementById("id_quitar_servicio").disabled = false;
        enviarPaso(1,1,{parent: ss_total.value-1});
    })
}

function quitar_servicios(){
    const quitar = document.getElementById("id_quitar_servicio");
    const ss_total = document.getElementById("id_subservicios_total");

    quitar.addEventListener("click", (e) => {
        ss_total.value = parseInt(ss_total.value) - 1;
        divEliminado = "#id_sub_servicio_content_" + ss_total.value;
        document.querySelector(divEliminado).remove();

        if (ss_total.value < 2) {
            e.target.disabled = true;
        }
    })
}

function pasosEstado() {
    if (pasoVal === 1) {
        funcionPaso1(subpasoVal);
    } else if (pasoVal === 2) {
        funcionPaso2();
    } else if (pasoVal === 3) {
        funcionPaso3(subpasoVal);
    }
}
// eventListener Functions
function no_name(event) {
    if (event.target.value !== ""){
        const parentTarget = event.target.parentNode.id;                  
        enviarPaso(1,2, {parent: parentTarget[parentTarget.length - 1]});
    }
}
function enviar_pre(event) {
    const formulario = document.getElementById("id_formulario_OS");
    const parentDivlist = event.target.parentNode.id.split("_");
    const paso = parentDivlist[2];
    let sub_servicio;
    if(isNaN(parentDivlist[3])) {
        sub_servicio = parentDivlist[4];
    } else {
        sub_servicio = parentDivlist[3];
    }
    let formulario_pasos = new Array();
    let formulario_contador = 0;
    let continuar = false;
    if (paso === "2") {
        let missing_fields = 0;
        const elementos = ["id_sitio_", "id_servicioContratado_", "id_epp_", "id_atencion_", "id_recoleccion_", "id_entrega_", "id_razonsocial_"]
        elementos.forEach(item => {
            form_element = formulario.elements.namedItem(item + sub_servicio);
            if (form_element === null) {
                missing_fields++;
            }
        })
        if (missing_fields > 4) {
            alert("Aún hay elementos que no han sido seleccionados.")
            formulario.elements.namedItem("id_servicioContratado_" + sub_servicio).focus();
        } else {
            elementos.forEach(item => {
                form_element = formulario.elements.namedItem(item + sub_servicio);
                if (form_element != null) {
                    if (form_element.value === "") {
                        const labels = document.getElementsByTagName('label');
                        for(let i = 0;i < labels.length; i++) {
                            if (labels[i].htmlFor === form_element.id) {
                                sub_num = parseInt(sub_servicio) + 1;
                                lab = labels[i].innerHTML.slice(0,-1);
                                alert(`El campo "${lab}" del servicio "${sub_num}" no ha sido seleccionado.`)
                                form_element.focus();
                            }
                        }
                    } else {
                        formulario_pasos.push(form_element.name);
                        formulario_contador++;
                    }
                }
            })
        }
        if (formulario_contador === 7 - missing_fields) {
            enviarPaso(1,3,{parent: sub_servicio, form: formulario_pasos});
        }
    } else if (paso === "3") {
        let missing_fields = 0;
        const elementos = ["id_certificado_", "id_facturacion_", "id_instrumento_"]
            elementos.forEach(item => {
            form_element = formulario.elements.namedItem(item + sub_servicio);
            if (form_element === null) {
                missing_fields++;
            }
        })
        if (missing_fields > 2) {
            alert("Aún hay elementos que no han sido seleccionados.")
            formulario.elements.namedItem("id_certificado_" + sub_servicio).focus();
        } else {
            elementos.forEach(item => {
                form_element = formulario.elements.namedItem(item + sub_servicio);
                if (form_element != null) {
                    if (form_element.value === "") {
                        const labels = document.getElementsByTagName('label');
                        for(let i = 0;i < labels.length; i++) {
                            if (labels[i].htmlFor === form_element.id) {
                                sub_num = parseInt(sub_servicio) + 1;
                                lab = labels[i].innerHTML.slice(0,-1);
                                alert(`El campo "${lab}" del servicio "${sub_num}" no ha sido seleccionado.`)
                                form_element.focus();
                            }
                        }
                    } else {
                        formulario_pasos.push(form_element.name);
                        formulario_contador++;
                    }
                } else {
                    if (item.search('instrument')) {
                        const instruments = document.getElementById(item + sub_servicio).querySelectorAll("input[type='checkbox']");
                        const links_edit = document.getElementById(item + sub_servicio).querySelectorAll("a");
                        if (instruments.length == 0) {
                            alert("Ningún instrumento ha sido seleccionado.");
                            document.getElementById("listado_" + sub_servicio).focus();
                        } else {
                            const labels = ['id_servicio', 'id_vigencia', 'observaciones_ios']
                            links_edit.forEach(link => {
                                const link_id = link.id[link.id.length - 1];
                                for (let i= 0; i < labels.length; i++) {
                                    const form_element = formulario.elements.namedItem(`${labels[i]}_${sub_servicio}_${link_id}`);
                                    if (form_element.value === "") {
                                        alert(`El campo "${form_element.previousSibling.textContent}" del instrumento "${link.previousElementSibling.textContent.slice(1)}" no ha sido seleccionado.`)
                                        form_element.focus();
                                        missing_fields++;
                                    } else {
                                        formulario_pasos.push(form_element.name);
                                        formulario_contador++;
                                    }
                                }
                            })
                        }
                        let miss = 2 + instruments.length*3;
                        if (formulario_contador != 2 && formulario_contador === miss) {
                            // enviarPaso(2,1,{parent: sub_servicio, form: formulario_pasos});
                            const class_active = document.querySelectorAll(".active");
                            class_active.forEach(item => {
                                if(item.nextElementSibling == event.target.parentNode.parentNode) {
                                    item.classList.toggle("active");
                                    event.target.parentNode.parentNode.style.maxHeight = null;
                                    event.target.parentNode.parentNode.style.padding = null;
                                }
                            })
                        }
                    }
                }
            })
        }
        
    }
}

//Función que se encarga de mandar el formulario relacionado al paso 2
function datos_instrumentos(event) {
    const instrument = event.target.parentNode.parentNode;
    const id_instrumento = event.target.name;
    const id = id_instrumento.split("_")[2];

    if (event.target.checked) {
        instrument.role = "";
        const new_instrument = instrument.cloneNode(true);
        new_instrument.addEventListener("change", remove_instrument);
        instrument.style.display = "none";
        
        const instrument_destiny = document.getElementById(id_instrumento);
        if(!instrument_destiny.querySelector("table")){
            let nueva_tabla = document.createElement( "table" );
            let col_grupo = document.createElement( "colgroup" );
            let thead = document.createElement( "thead" );
            let tbody = document.createElement( "tbody" );

            const col_porcentajes = ["5%", "15%", "40%", "15%", "15%", "10%"];
            const col_head = ["", "ID Instrumento", "ID Sitio", "Marca", "Modelo", ""];
            for(let i= 0; i<col_head.length; i++) {
                const porcentaje = col_porcentajes[i];
                const head = col_head[i];

                const col = document.createElement( "col" );
                col.style.width = porcentaje;
                col_grupo.appendChild(col);

                const th = document.createElement( "th" );
                th.innerHTML = head;
                thead.appendChild(th);
            }
            nueva_tabla.appendChild(col_grupo);
            nueva_tabla.appendChild(thead);
            nueva_tabla.appendChild(tbody);

            instrument_destiny.appendChild(nueva_tabla);
            instrument_destiny.classList.remove("selected-items")
        }

        instrument_destiny.querySelector("tbody").appendChild(new_instrument);
        const new_row = document.createElement( "tr" );
        new_row.classList.add("tr-no-hover");
        const new_td = document.createElement( "td" );
        new_td.id = "id_instrument_data_" + id + "_" + event.target.value;
        new_td.classList.add("instrument_content_data");
        new_td.colSpan = "6";
        new_row.appendChild(new_td)
        instrument_destiny.querySelector("tbody").appendChild(new_row);

        new_instrument.addEventListener("click", showDataInst, false);
        

        enviarPaso(2,1,{parent:id, position:event.target.value});
    }
    // height_control(height_var);
}

function remove_instrument(event) {
    const instrument = event.target.parentNode.parentNode;
    const id_instrumento = event.target.name;
    const id = id_instrumento.split("_")[2];
    const instrument_data = document.getElementById(`id_instrument_data_${id}_${event.target.value}`).parentNode;
    const instrument_table = document.getElementById(`instrument_table_${id}`).querySelector("tbody");
    for(let i= 0; i<instrument_table.children.length; i++) {
        const item = instrument_table.children[i];
        if(item.querySelector("input").value === instrument.querySelector("input").value){
            item.style.display = "";
            item.querySelector("input").checked = false;
        }
    }
    const height = instrument_data.scrollHeight;
    instrument.remove();
    instrument_data.remove();
    height_control(height);
}

function agregar_campo_img(event) {
    const ref = event.target.parentNode.nextElementSibling;
    const id_ref = ref.htmlFor.split("_");
    const parent = id_ref[2];
    const instrument = id_ref[3];

    let total_img = document.getElementById(`id_TOTAL_images_${parent}_${instrument}`);
    if(total_img.value < 5){
        let new_img = ref.cloneNode(true);
    
        new_img.htmlFor = `id_imagen_${parent}_${instrument}_${total_img.value}`;
        const img_field = new_img.children[0];
        img_field.name = `imagen_${parent}_${instrument}_${total_img.value}`;
        img_field.id = `id_imagen_${parent}_${instrument}_${total_img.value}`;
    
        ref.parentNode.appendChild(new_img);
        total_img.value = parseInt(total_img.value) + 1;
        if(total_img.value > 4) {
            event.target.classList.remove("icon-active");
            event.target.classList.add("disabled");
        }
        height_control();
    }
}

function ocultar_datos_instrumento(event) {
    event.target.parentNode.style.display = "none";
    height_control(50);
}

function submit_formulario() {
    //Validación de campos de paso 3
    const fecha_hora = document.getElementById("id_dia_servicio");
    fecha_hora.addEventListener("change", (event) => {
        const fecha = fecha_hora.value.split("T")[0].split("-")
        const hora = String(fecha_hora).split("T")[1];

        const date_js = new Date(fecha);
        if (date_js.getDay() == 0) {
            alert("Los domingos no prestamos servicios.");
            fecha_hora.focus();
        }

    })
    const submit_button = document.getElementById("submit_form");
    submit_button.addEventListener("click", enviar_formulario)
}

function enviar_formulario() {
    const formulario = document.getElementById("id_formulario_OS");
    enviarPaso(4, 1, 0)
}
//Funciones para ejecutar sobre distintos pasos durante el llenado del formulario
function funcionPaso1(subpaso) {
    agregar_funcion_add();
    if (subpaso === 1) {
        const clienteEmpresa = document.getElementById('id_id_cliente');

        clienteEmpresa.addEventListener('change', (event) => {
            if (event.target.value !== "") {
                enviarPaso(1,1,{parent: 0});
                agregarFunciones(event);
            }
        });
    } else if (subpaso === 2) {
        const selects = document.querySelectorAll("select");
        selects.forEach(item => {
            id = item.id;
            if(id.includes("sitio") || id.includes("contacto")) {
                item.addEventListener('change', event => {
                    if(event.target.value !== "") {
                        agregarFunciones(event);
                    }
                })
            }
        })
        const servicio_items = document.querySelectorAll(".js_class_2")
        servicio_items.forEach(item =>{
            item.addEventListener('change', no_name)
        })
        const botones = document.querySelectorAll(".btn_selector");
        botones.forEach(boton => {
            boton.addEventListener("click", enviar_pre);
        })

        submit_formulario();
    }
}

function funcionPaso2(subpaso) {
    agregar_funcion_add();
    const selects = document.querySelectorAll('select');
    selects.forEach(item => {
        id = item.id;
        if(id.includes('facturacion') || id.includes('certificado')) {
            item.addEventListener("change", event => {
                if(event.target.value !== "") {
                    agregarFunciones(event);
                }
            });
        }
    })
    const botones = document.querySelectorAll(".btn_selector");
    botones.forEach(boton => {
        const parent = boton.parentNode.id;
        if (parent.search("paso_3") != -1) {
            boton.addEventListener("click", enviar_pre);
            const div_instr = boton.parentNode.parentNode.children[1];
            div_instr.querySelectorAll("input[type='checkbox']").forEach(instrumento => {
                instrumento.addEventListener("change", datos_instrumentos);
            })
        }
    })
}

function funcionPaso3() {
    agregar_funcion_add()
    const botones_img = document.getElementsByName("add-img-field");
    botones_img.forEach(img_add => {
        img_add.addEventListener("click", agregar_campo_img);
    });
}

function peticionAJAX(request) {
    /** Función que hace una llamada de tipo AJAX */
    //Crear objeto
    const xhr = new XMLHttpRequest();
    //Abrir la conexión
    xhr.open('POST', '/orders/service_order/', true);
    //Pasar los datos
    xhr.onload = function() {
        if(this.status === 200) {
            if (JSON.parse(xhr.responseText).status === 248) {
                window.location.href = JSON.parse(xhr.responseText).url;
            } else {
                const responseText = JSON.parse(xhr.responseText);
                if(responseText.accion) {
                    objetosAdministrar(responseText);
                } else {
                    renderizarFormulario(responseText);
                }
            }
        } else {
            console.log(this.status);
        }
    }
    //Encabezado para identificar un AJAX request en django
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    //Enviar los datos
    xhr.send(request);
}

function renderizarFormulario(responseText) {
    const { paso, sub_paso, html, id_parent } = responseText
    id_table = 0;
    if (paso === 1) {
        if (sub_paso === 2) {
            const total_sub_servicios = document.getElementById("id_subservicios_total").value - 1;
            const divForm = document.getElementById('id_paso_2_sitio_' + total_sub_servicios);
            divForm.innerHTML = html;
            const divF = document.getElementById('id_paso_2_servicio_' + id_parent);
            
            if(!(document.getElementById("siguiente_paso_2_" + id_parent))) {
                const boton_a_2 = document.createElement( "input" ); 
                boton_a_2.type = "button";
                boton_a_2.value = "Siguiente Paso";
                boton_a_2.id = "siguiente_paso_2_" + id_parent;
                boton_a_2.classList.add('button');
                boton_a_2.classList.add('btn_selector');
                divForm.parentNode.appendChild(boton_a_2);
            }

            //Agregar paso 3 de formulario de OS
            const paso_3_div = document.getElementById("id_ordenServicio-form");
            paso_3_div.innerHTML = responseText.html_extra;
            document.getElementById("id_paso_5").style.display = "block";
            document.getElementById("submit_form").style.display = "inline";
            
            document.getElementById('id_sub_paso_formulario').value = sub_paso;
            subpasoVal = sub_paso;
            document.getElementById('id_contenedor_sub_servicios').style.display= "block";

            document.getElementById('id_paso_formulario').value = paso;
            pasoVal = paso;
        } else if (sub_paso === 3) {
            const divForm = document.getElementById('id_paso_2_servicio_' + id_parent);
            divForm.innerHTML = html;

            document.getElementById('id_sub_paso_formulario').value = sub_paso;
            subpasoVal = sub_paso;
            document.getElementById('id_paso_formulario').value = paso;
            pasoVal = paso;
            height_control();
        }
    } 
    else if (paso === 2) {
        const div_instr = document.getElementById('id_paso_3_instrumento_' + id_parent);
        const div_certi = document.getElementById('id_paso_3_certificado_' + id_parent);
        const div_factu = document.getElementById('id_paso_3_facturacion_' + id_parent);

        div_instr.innerHTML = html.lista_instrumentos;
        // div_instr.innerHTML = html.instrumentos
        div_certi.innerHTML = html.certificado;
        div_factu.innerHTML = html.facturacion;

        const boton_3 = document.createElement( "input" );
        boton_3.type = "button";
        boton_3.id = "siguiente_paso_3_" + id_parent;
        boton_3.value = "Siguiente paso";
        boton_3.classList.add("button");
        boton_3.classList.add("btn_selector");
        div_factu.appendChild(boton_3);

        document.querySelector(".paso_3_instrumento").removeAttribute("content");
        document.getElementById('id_paso_formulario').value = paso;
        document.getElementById('id_sub_paso_formulario').value = sub_paso;
        pasoVal = paso;
        subpasoVal = sub_paso;
        tablaFuncionalidad(html.id_table);
        height_control();
    } else if (paso === 3) {
        const divForm = document.getElementById(`id_instrument_data_${id_parent}_${responseText.instrument}`);
        divForm.innerHTML = html;

        document.getElementById('id_paso_formulario').value = paso;
        document.getElementById('id_sub_paso_formulario').value = sub_paso;
        pasoVal = paso;
        subpasoVal = sub_paso;
        height_control();
    }
    pasosEstado(pasoVal,subpasoVal);
}

function servicioBtn(parent, servicio, form_data= 0) {
    const request = new FormData();
    request.append("csrfmiddlewaretoken", django_variables.token);
    request.append("servicio", servicio);
    request.append("elemento", parent.id);

    if (form_data == 0) {
        if (parent.id.includes("instrumento")) {
            const id_empresa = document.getElementById("id_id_cliente");
            request.append("valor", id_empresa.value);
        } else {
            request.append("valor", parent.value)
        }
    } else {
        if(document.getElementById("id_areamagnitud")) {
            let areamagnitud = [];
            const childrens = document.getElementById("id_areamagnitud").children;
            for(i=0; i<childrens.length; i++) {
                if(childrens[i].selected) {
                    areamagnitud.push(childrens[i].value);
                }
            }
            request.append("areamagnitud", areamagnitud);
        }
        const val_ele = document.getElementById(parent).value;
        request.set("elemento", parent);
        request.append("form", JSON.stringify(form_data));
        request.append("elemento_valor", val_ele);
    }
    peticionAJAX(request);
}

function enviarPaso(paso, subpaso, ...kwargs) {
    kwargs = kwargs[0];
    //Verificación de campos de paso 1
    const formulario = document.getElementById("id_formulario_OS");
    //Recopilación de datos para petición
    let requestNext = new FormData();
    //Credenciales
    requestNext.append('csrfmiddlewaretoken', django_variables.token);
    requestNext.append('paso', paso);
    requestNext.append('sub_paso', subpaso);
    requestNext.append("id_parent", kwargs.parent);
    requestNext.append('AJAXCall', 1);
    //Variables a enviar
    if (paso==1) {
        if (subpaso==1) {
            requestNext.append("id_empresa", formulario.id_id_cliente.value);
            requestNext.append('submit', 0);
        } else if (subpaso==2) {
            servicioContratado = formulario.elements.namedItem("id_servicioContratado_" + kwargs.parent)
            requestNext.append('servicioContratado', servicioContratado.value);
            requestNext.append('submit', 0)
        } else if (subpaso==3) {
            requestNext.append("id_empresa", formulario.id_id_cliente.value);
            kwargs.form.forEach(name => {
                val = formulario.elements.namedItem(name).value;
                requestNext.append(name,val);
            });
            requestNext.append('submit', 'next');
        }
    } else if (paso===2) {
        requestNext.append("posicion", kwargs.position);
        requestNext.append("submit", 'next');
    } else if (paso === 4) {
        requestNext = new FormData(formulario);
        requestNext.append("AJAXCall",0);
        // requestNext.append("form", formulario);
    }
    peticionAJAX(requestNext);
}

function multipleImagen() {
    const agregar_img = document.getElementById('agregar_imagen');
    agregar_img.addEventListener('click', (e) => {
        const img = document.getElementById('id_imagen_1');
        const parent = img.parentNode;
        const new_img = img.cloneNode(true);
        const total_img = document.getElementById('image_total_form');

        new_img.id = "id_imagen_" + total_img.value;
        new_img.name = "imagen_" + total_img.value;
        total_img.value = parseInt(total_img.value) + 1;

        parent.insertBefore(new_img, img.nextSibling);
    })
}

function colapsar() {
    var coll = document.getElementsByClassName("colapsar");
    var i;
    
    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", add_element);
    }
}

function add_element() {
    this.classList.toggle("active");
    if (this.innerHTML.includes("Servicio:")) {
        this.classList.toggle("parent");
        var content = this.nextElementSibling;
        if (content.style.maxHeight){
            content.style.maxHeight = null;
            content.style.padding = null;
        } else {
            content.style.maxHeight = content.scrollHeight + 9.5 + "px";
            content.style.padding = "0.3rem 1rem";
        }
    } else {
        var content = this.nextElementSibling;

        if (content.style.maxHeight){
            content.style.maxHeight = null;
            content.style.padding = null;
        } else {
            var child_size = content.scrollHeight;
            content.style.maxHeight = content.scrollHeight + 9.5 +  "px";
            content.style.padding = "0.3rem 1rem";
        }

        var parent_content = document.querySelectorAll(".parent");
        let j;

        for (j = 0; j < parent_content.length; j++) {
            var child = parent_content[j].nextElementSibling;
            var total_size = child.scrollHeight + child_size;
            child.style.maxHeight = total_size + "px";
        }
    }
}

function height_control(element_height = 0) {
    const button_col = document.querySelectorAll(".active");
    button_col.forEach(item => {
        var child = item.nextElementSibling;
        child.style.maxHeight = (child.scrollHeight - element_height) + "px";
    })
}
function agregarFunciones(event) {
    const div_icons = event.target.parentNode.nextElementSibling;
    const icons = div_icons.querySelectorAll(".icon");
    
    icons.forEach(icon => {
        if(icon.classList.contains("disabled")) {
            icon.classList.remove("disabled");
            icon.classList.add("icon-active");
        }
        
        let id = icon.src.split("/");
        id = id[id.length - 1];

        if(id.includes("edit")) {
            icon.addEventListener("click", editar_objetos);
        } else if(id.includes("detail")) {
            icon.addEventListener("click", detalles_objetos)
        }
    });
}

function agregar_funcion_add() {
    const icons = document.querySelectorAll(".icon");
    icons.forEach(icon => {
        src = icon.src.split("/");
        src = src[src.length - 1];
        if(!(icon.name.includes("img"))) {
            if(src.includes("add")) {
                icon.addEventListener("click", agregar_objetos);
            }
        }
        
    })
}

function agregar_objetos(event) {
    let parent;
    if(!event.target.id.includes("instrumento")){
        const parent_elements = event.target.parentNode.previousElementSibling.children;
        parent = parent_elements[parent_elements.length - 1];
    } else {
        parent = event.target.parentNode.parentNode.children[1];
    }

    servicioBtn(parent, "formulario")
}

function editar_objetos(event) {
    const parent_elements = event.target.parentNode.previousElementSibling.children;
    const parent = parent_elements[parent_elements.length - 1];
    
    servicioBtn(parent, "actualizar");
}

function detalles_objetos(event) {
    const parent_elements = event.target.parentNode.previousElementSibling.children;
    const parent = parent_elements[parent_elements.length - 1];
    
    servicioBtn(parent, "detalles");
}

function objetosAdministrar(responseText) {
    const { model, parent, accion } = responseText;
    let id;
    if (parent.includes("cliente")) {
        id = "cliente-crear";
    } else if (parent.includes("sitio")) {
        id = "sitio-crear";
    } else if (parent.includes("contacto")) {
        id = "contacto-crear";
    } else if (parent.includes("certificado")) {
        id = "certificado-crear";
    } else if (parent.includes("facturacion")) {
        id = "facturacion-crear";
    } else if (parent.includes("instrumento")) {
        id = "instrumento-crear";
    }

    if (accion === "detalles" || accion === "crear" || accion === "actualizar") {
        const div = document.getElementById("divCenter");
        div.querySelector(".divContent").innerHTML = model;
        div.style.display = "block";
        div.style.overflow = "scroll";
        document.querySelector("body").classList.add("fijar-body");

        if (accion === "crear" || accion === "actualizar") {
            const form_div = document.getElementById(id).querySelector(".form-content");
            const button_submit = document.createElement( "BUTTON" );
            button_submit.classList.add("crear-btn");
            button_submit.classList.add("button");
            button_submit.type = "button";
            button_submit.textContent = accion[0].toUpperCase() + accion.slice(1, accion.length);
            form_div.appendChild(button_submit);
            
            button_submit.addEventListener("click", (event) => {
                crear_objeto(event, parent, accion);
            });
        }
    } else if (accion === "actualizar_elemento") {
        console.log("Aquí empezamos")
        update_element(accion, parent, model);
    }
}

function crear_objeto(event, parent, accion) {
    const form_id = event.target.parentNode.parentNode.id;
    const form_elements = document.getElementById(form_id).elements;
    let form_data = new Object();

    for(let i = 0; i < form_elements.length - 1; i++) {
        let element = form_elements[i];
        if(element.type != "checkbox") {
            if(element.value === "") {
                error_mensaje(element);
                return
            } else {
                form_data[element.name] = element.value;
            }
        } else {
            form_data[element.name] = element.checked;
        }
    }
    if (!form_id.includes("cliente")) {
        const cliente = document.getElementById("id_id_cliente");
        form_data["id_empresa"] = cliente.value;
    }
    servicioBtn(parent, accion, form_data);
}

function error_mensaje(element) {
    const error_div = document.querySelector(".error-card");
    const input = element.parentNode.textContent.trim().slice(0,-1);

    const mensaje = `ERROR: El elemento "${input}" no ha sido llenado`
    error_div.textContent = mensaje;
    error_div.style.display = "block";
    element.focus();

    setTimeout(function() {
        error_div.style.display = "none";
    }, 3500);
}

function update_element(accion, parent, model) {
    document.getElementById("divCenter").style.display = "none";
    document.querySelector("body").classList.remove("fijar-body");
    let changed_val = false;

    const update_element = document.getElementById(parent);
    if(parent.includes("instrumento")) {
        update_element.innerHTML = model.html;
        tablaFuncionalidad(model.id_table);
        agregar_funcion_add()
        document.getElementById(model.id_table).querySelectorAll("input[type='checkbox']").forEach(instrumento => {
            instrumento.addEventListener("change", datos_instrumentos);
        })
        height_control();
    } else {
        const options = update_element.children;
        for(let i= 0; i < options.length; i++) {
            if(options[i].value == model.value) {
                options[i].textContent = model.option;
                changed_val = true;
            }
        }
    
        if(!changed_val) {
            console.log("No debería de estar aquí")
            const option = document.createElement( "option" );
            option.textContent = model.option;
            option.value = model.value;
            option.selected = true;
            update_element.appendChild(option);
            dispararEvento(update_element, "change");
        }
    }
}

function dispararEvento(element, tipo) {
    // IE9+ and other modern browsers
    if ('createEvent' in document) {
        var e = document.createEvent('HTMLEvents');
        e.initEvent(tipo, false, true);
        element.dispatchEvent(e);
    } else {
        // IE8
        var e = document.createEventObject();
        e.eventType = tipo;
        element.fireEvent('on' + e.eventType, e);
    }
}

function tablaFuncionalidad(id_table) {
    $("#" + id_table).DataTable({
        columnDefs: [{ type: "date", targets: [3] }],
    });
    
    const tabla = document.getElementById(id_table);
    const tr = tabla.querySelector("tbody").children;
    for(let i= 0; i<tr.length; i++) {
        const item = tr[i];
        item.addEventListener("click", checkedCheckbox, false);
    }
}

function checkedCheckbox(event) {
    if(event.target.nodeName === "TD") {
        const check_but = event.target.parentNode.querySelector("input[type='checkbox']");
        check_but.checked = !check_but.checked;
        dispararEvento(check_but,"change");
    }
}

function showDataInst(event) {
    const dataRow = event.target.parentNode.nextElementSibling;
    if(!(event.target.type === "checkbox")) {
        if(dataRow.style.display === "none") {
            dataRow.style.display = "";
            height_control();
        } else {
            height_control(dataRow.scrollHeight - 25);
            dataRow.style.display = "none";
        }
    }
}

