

class HotDog {
    constructor(
        public bread: string,
        public ketchup?: boolean,
        public mustard?: boolean,
        public kraut?: boolean
    ) { }

    addKetchup() {
        this.ketchup = true;
        return this;
    }
    addMustard() {
        this.mustard = true;
        return this;
    }
    addKraut() {
        this.kraut = true;
        return this;
    }
}

const myLunch = new HotDog('non-veg')
    .addKetchup()
    .addMustard()
    .addKraut();

//source - https://fireship.io/lessons/typescript-design-patterns/