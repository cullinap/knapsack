#### algorithms to solve multi-dimensional 0-1 knapsack problem

https://en.wikipedia.org/wiki/Knapsack_problem#Multi-dimensional_knapsack_problem.

Values are assigned to items with two paramenters (weight and volume in this case). The objective is to find the highest value while constrained to a limit on weight and volume. More concretely the goal is to fit the most in a knapsack while obtaining the highest value.

The algorithm calls upon itself to find the optimal combination max values at various states throughout the process. Inspiration came from professor Dennis Bricker: http://user.engineering.uiowa.edu/~dbricker/.
