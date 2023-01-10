class Ingreso extends Dato {
    static contadorIngresos = 0;
    constructor(descripcion, valor) {
        super(descripcion, valor);
        this.id = ++Ingreso.contadorIngresos;
    }

    getId() {
        return this.id;
    }
}