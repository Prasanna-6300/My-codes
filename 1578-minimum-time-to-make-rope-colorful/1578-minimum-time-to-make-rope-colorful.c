int minCost(char* colors, int* neededTime, int n) {
    int totalTime = 0;
    int maxTime = neededTime[0];

    for (int i = 1; i < n; i++) {
        if (colors[i] == colors[i - 1]) {
            totalTime += (neededTime[i] < maxTime) ? neededTime[i] : maxTime;
            if (neededTime[i] > maxTime)
                maxTime = neededTime[i];
        } else {
            maxTime = neededTime[i];
        }
    }
    return totalTime;
}

