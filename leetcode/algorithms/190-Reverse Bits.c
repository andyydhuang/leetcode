uint32_t reverseBits(uint32_t n) {
    uint32_t r_n = 0;
    for (int k = 0; k < 32; k++) {
        int temp = n & 1;
        n = n >> 1;
        //printf("%d\n",temp);
        r_n |= (uint32_t)(temp) << (31-k);
    }
    
    return r_n;
}