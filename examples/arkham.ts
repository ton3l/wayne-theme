class Gotham {
    private villains: string[];
    public hero: string;

    constructor() {
        this.villains = ["Joker", "Harley Quinn", "Two-Face"];
        this.hero = "Batman";
    }

    addVillain(villain: string) {
        this.villains.push(villain);
    }

    getVillains() {
        return this.villains;
    }
}
