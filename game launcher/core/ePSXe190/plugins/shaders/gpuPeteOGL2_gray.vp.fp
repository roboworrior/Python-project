!!ARBfp1.0

TEMP  color0;

PARAM toGray = { 0.3, 0.59, 0.11, 0.0 };

TEX	color0, fragment.texcoord[ 0 ], texture[ 0 ], 2D;

DP3	result.color, color0, toGray;

END
