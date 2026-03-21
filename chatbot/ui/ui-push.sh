rm -r ~/symbolfigures.io/bitloops/chatbot/*
cp -r ~/symbolfigures/bitloops/chatbot/ui/out/* ~/symbolfigures.io/bitloops/chatbot
aws s3 rm --recursive s3://symbolfigures.io/bitloops/chatbot/
aws s3 cp --recursive ~/symbolfigures.io/bitloops/chatbot/ s3://symbolfigures.io/bitloops/chatbot/
aws cloudfront create-invalidation \
        --distribution-id E30DZIU4LRVUNW \
        --paths /bitloops/chatbot/*
