const ingresos = [
    new Ingreso('Salario', 20000),
    new Ingreso('Venta auto', 50000),
]

const egresos = [
    new Egreso('Renta', 4000),
    new Egreso('Ropa', 800),
]

const cargarCabecero = () => {
    let presupuesto = totalIngresos() - totalEgresos();
    let porcentajeEgreso = totalEgresos() / totalIngresos();
    document.getElementById('presupuesto').innerHTML = formatoMoneda(presupuesto);
    document.getElementById('porcentaje').innerHTML = formatoPorcentaje(porcentajeEgreso);
    document.getElementById('ingresos').innerHTML = formatoMoneda(totalIngresos());
    document.getElementById('egresos').innerHTML = formatoMoneda(totalEgresos());
}

const totalIngresos = () => {
    let totalIngresos = 0;
    for (const ingreso of ingresos) {
        totalIngresos += ingreso.getValor();
    }
    return totalIngresos;
}

const totalEgresos = () => {
    let totalEgreso = 0;
    for (const egreso of egresos) {
        totalEgreso += egreso.getValor();
    }
    return totalEgreso;
}

const formatoMoneda = (valor) => {
    return valor.toLocaleString('es-MX', { style: 'currency', currency: 'MXN', minimumFractionDigits: 2 });
}

const formatoPorcentaje = (valor) => {
    return valor.toLocaleString('es-MX', { style: 'percent', minimumFractionDigits: 2 })
}

const cargarApp = () => {
    cargarCabecero();
    cargarIngresos();
    cargarEgresos();
}

const cargarIngresos = () => {
    let ingresosHTML = '';
    for (const ingreso of ingresos) {
        ingresosHTML += creadorIngresoHTML(ingreso);
    }
    document.getElementById('lista-ingresos').innerHTML = ingresosHTML;
}

const creadorIngresoHTML = (ingreso) => {
    let ingresoHTML = `
    <div class="elemento limpiarEsitlos">
        <div class="elemento_descipcion">${ingreso.getDescripcion()}</div>
        <div class="derecha limpiarEstilos">
            <div class="elemento_valor">${formatoMoneda(ingreso.getValor())}</div>
            <div class="elemento_eliminar">
                <button class="elemento_eliminar--btn" onclick="eliminarIngreso(${ingreso.getId()})">
                    <ion-icon name="close-circle-outline"></ion-icon>
                </button>
            </div>
        </div>
    </div>
    `;
    return ingresoHTML;
};

const cargarEgresos = () => {
    let egresosHTML = '';
    for (const egreso of egresos) {
        egresosHTML += crearEgresoHTML(egreso);
    }
    document.getElementById('lista-egresos').innerHTML = egresosHTML;
};

const crearEgresoHTML = (egreso) => {
    let egresoHTML = `
    <div class="elemento limpiarEsitlos">
        <div class="elemento_descipcion">${egreso.getDescripcion()}</div>
        <div class="derecha limpiarEstilos">
            <div class="elemento_valor">${formatoMoneda(egreso.getValor())}</div>
            <div class="elemento_porcentaje">-21%</div>
            <div class="elemento_eliminar">
                <button class="elemento_eliminar--btn" onclick="eliminarEgreso(${egreso.getId()})">
                    <ion-icon name="close-circle-outline"></ion-icon>
                </button>
            </div>
        </div>
    </div>
    `;
    return egresoHTML;
};

const eliminarEgreso = (id) => {
    let indiceEliminar = egresos.findIndex(egreso => {
        return egreso.getId() == id;
    });

    egresos.splice(indiceEliminar, 1);
    cargarCabecero();
    cargarEgresos();
}

const eliminarIngreso = (id) => {
    let indiceEliminar = ingresos.findIndex(ingreso => {
        return ingreso.getId() == id;
    });

    ingresos.splice(indiceEliminar, 1);
    cargarCabecero();
    cargarIngresos();
}

const agregarDato = () => {
    let tipo = document.getElementById('tipo').value;
    let descripcion = document.getElementById('descripcion').value;
    let valor = document.getElementById('valor').value;

    if(valor.length && descripcion.length) {
        if(tipo == 'ingreso'){
            ingresos.push(new Ingreso(descripcion, Number(valor)));
            cargarCabecero();
            cargarIngresos();
        } else {
            egresos.push(new Egreso(descripcion, Number(valor)));
            cargarCabecero();
            cargarEgresos();
        }
    }
}

document.body.onload = () => {
    cargarApp();
};
