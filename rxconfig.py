import reflex as rx

config = rx.Config(
    app_name="proyectoll",
    plugins=[rx.plugins.TailwindV3Plugin()],
    db_url='postgresql://postgres.yakhvcawktkeaylcvhcu:XTNZc7lIvnVllwtc@aws-0-us-east-1.pooler.supabase.com:6543/postgres'
)

#postgresql://postgres.yakhvcawktkeaylcvhcu:XTNZc7lIvnVllwtc@aws-0-us-east-1.pooler.supabase.com:6543/postgres