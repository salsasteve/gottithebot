import { SupabaseClient } from "@supabase/supabase-js";

export const getProfile = async (
  userId: string,
  supabase: SupabaseClient
): Promise<any> => {
  let { data } = await supabase
    .from("profiles")
    .select(`username, website, avatar_url`)
    .eq("id", userId)
    .single();
  return data;
};

export const downloadImage = async (path: string, supabase: SupabaseClient) => {
  let src = "";
  try {
    const { data, error } = await supabase.storage
      .from("avatars")
      .download(path);
    if (error) throw error as any;
    src = URL.createObjectURL(data);
  } catch (error) {
    console.error("Error downloading image: ", error.message);
  }
  return src;
};
