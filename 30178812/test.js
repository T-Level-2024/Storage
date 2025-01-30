const car = {
	brand: "Toyota",
	model: "Corolla",
	year: "2020",
	getDetails: function() {
		return "${this.brand} ${this.model}, ${this.year}";
	}
};
console.log(car.getDetails());

let array = string[];
array = ["Movie 1", "Movie 2", "Movie 3"];
array.append("Movie 4");
array.shift();
for(let i = 0; i < array.len; i++){
	console.log(array[i]);
}

const calculate_total = numbers => {
	let total = 0;
	for(let i = 0; i < numbers.len; i++){
		total += numbers[i];
	}
	return console.log(total);
};